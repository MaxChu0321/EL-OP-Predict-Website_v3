import pandas as pd
from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import ValidationError
from io import BytesIO
import joblib
import logging
import json
from setting import *
from scripts import parse_feature, get_derived_features, standardize_df, predict_ER, predict_surv, parse_feature_OP, get_derived_features_OP,get_derived_features_OP_pre
from models import PatientData_ER, PatientData_Surv, PatientData_ER_OP, PatientData_ER_OP_pre

# Initial
## setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
# get root logger
logger = logging.getLogger(__name__)
logger.info("Logging...")

logger.info("Import EL-RFA model...")
ELRFA_ER_cli_sEstimator = joblib.load(ELRFA_ER_cli_sMODEL)
ELRFA_ER_cli_bEstimator = joblib.load(ELRFA_ER_cli_bMODEL)
ELRFA_ER_cli_2DRad_sEstimator = joblib.load(ELRFA_ER_cli_2DRad_sMODEL)
ELRFA_ER_cli_2DRad_bEstimator = joblib.load(ELRFA_ER_cli_2DRad_bMODEL)
ELRFA_ER_cli_Rad_sEstimator = joblib.load(ELRFA_ER_cli_Rad_sMODEL)
ELRFA_ER_cli_Rad_bEstimator = joblib.load(ELRFA_ER_cli_Rad_bMODEL)
ELRFA_ER_cli_2DRad_DL_sEstimator = joblib.load(ELRFA_ER_cli_2DRad_DL_sMODEL)
ELRFA_ER_cli_2DRad_DL_bEstimator = joblib.load(ELRFA_ER_cli_2DRad_DL_bMODEL)
ELRFA_ER_cli_Rad_DL_sEstimator = joblib.load(ELRFA_ER_cli_Rad_DL_sMODEL)
ELRFA_ER_cli_Rad_DL_bEstimator = joblib.load(ELRFA_ER_cli_Rad_DL_bMODEL)
ELRFA_surv_cli_Estimator = joblib.load(ELRFA_surv_cli_MODEL)
ELRFA_surv_cli_2DRad_Estimator = joblib.load(ELRFA_surv_cli_2DRad_MODEL)
ELRFA_surv_cli_Rad_Estimator = joblib.load(ELRFA_surv_cli_Rad_MODEL)
ELRFA_surv_cli_2DRad_DL_Estimator = joblib.load(ELRFA_surv_cli_2DRad_DL_MODEL)
ELRFA_surv_cli_Rad_DL_Estimator = joblib.load(ELRFA_surv_cli_Rad_DL_MODEL)

logger.info("Get EL-RFA features...")
ELRFA_ER_cli_sFeatures = parse_feature(ELRFA_ER_cli_sEstimator)
ELRFA_ER_cli_bFeatures = parse_feature(ELRFA_ER_cli_bEstimator)
ELRFA_ER_cli_2DRad_sFeatures = parse_feature(ELRFA_ER_cli_2DRad_sEstimator)
ELRFA_ER_cli_2DRad_bFeatures = parse_feature(ELRFA_ER_cli_2DRad_bEstimator)
ELRFA_ER_cli_Rad_sFeatures = parse_feature(ELRFA_ER_cli_Rad_sEstimator)
ELRFA_ER_cli_Rad_bFeatures = parse_feature(ELRFA_ER_cli_Rad_bEstimator)
ELRFA_ER_cli_2DRad_DL_sFeatures = parse_feature(ELRFA_ER_cli_2DRad_DL_sEstimator)
ELRFA_ER_cli_2DRad_DL_bFeatures = parse_feature(ELRFA_ER_cli_2DRad_DL_bEstimator)
ELRFA_ER_cli_Rad_DL_sFeatures = parse_feature(ELRFA_ER_cli_Rad_DL_sEstimator)
ELRFA_ER_cli_Rad_DL_bFeatures = parse_feature(ELRFA_ER_cli_Rad_DL_bEstimator)
ELRFA_surv_cli_Features = parse_feature(ELRFA_surv_cli_Estimator)
ELRFA_surv_cli_2DRad_Features = parse_feature(ELRFA_surv_cli_2DRad_Estimator)
ELRFA_surv_cli_Rad_Features = parse_feature(ELRFA_surv_cli_Rad_Estimator)
ELRFA_surv_cli_2DRad_DL_Features = parse_feature(ELRFA_surv_cli_2DRad_DL_Estimator)
ELRFA_surv_cli_Rad_DL_Features = parse_feature(ELRFA_surv_cli_Rad_DL_Estimator)

logger.info("Import EL-OP model...")
ELOP_ER_cli = joblib.load(ELOP_ER_cli_MODEL)
ELOP_ER_multi = joblib.load(ELOP_ER_multi_MODEL)
ELOP_ER_precli = joblib.load(ELOP_ER_precli_MODEL)
ELOP_ER_premulti = joblib.load(ELOP_ER_premulti_MODEL)
logger.info("Get EL-OP features...")
ELOP_ER_cli_Features = parse_feature(ELOP_ER_cli)
ELOP_ER_multi_Features = parse_feature(ELOP_ER_multi)
ELOP_ER_precli_Features = parse_feature(ELOP_ER_precli)
ELOP_ER_premulti_Features = parse_feature(ELOP_ER_premulti)
logger.info("Initial API...")
app = FastAPI()

# CORS
origins = [
    "*"
    # "http://localhost:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Initialization complete.")


# Views
@app.get("/api/test")
def test():
    return ELRFA_ER_cli_sFeatures

@app.post("/api/early_recurrence/submit/case")
async def submit(request: Request):
    results = None  # 初始化結果變量
    form_data = await request.form()
    data_dict = {key: value for key, value in form_data.items() if not isinstance(value, UploadFile)}
    file: UploadFile = form_data.get("file")

    try:
        patient_data = PatientData_ER(**data_dict)
        patient_data_OP = PatientData_ER_OP(**data_dict)
        patient_data_OP_pre = PatientData_ER_OP_pre(**data_dict)
    except ValidationError as e:
        print("Validation Error:", e)
        return HTTPException(status_code=400, detail=f"Validation error: {e.errors()}")
        # return HTTPException(status_code=400, detail=f"Validation error: {e.errors()}")
    clinical_data_df = pd.DataFrame([patient_data.dict()])
    clinical_data_df_OP = pd.DataFrame([patient_data_OP.dict()])
    clinical_data_df_OP_pre = pd.DataFrame([patient_data_OP_pre.dict()])
    if file:
        file_contents = await file.read()
        try:
            if file.filename.endswith('.csv'):
                image_features_df = pd.read_csv( BytesIO( file_contents ) ).astype('float')
            elif file.filename.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
                image_features_df = pd.read_excel( BytesIO( file_contents ) ).astype('float')
            else:
                raise HTTPException(status_code=400, detail="Unsupported file format")
            
            complete_data_df = pd.concat([clinical_data_df, image_features_df], axis=1)
            complete_data_df_OP = pd.concat([clinical_data_df_OP, image_features_df], axis=1)
            complete_data_df_OP_pre = pd.concat([clinical_data_df_OP_pre, image_features_df], axis=1)
            if complete_data_df_OP.loc[0, 'Histologic grade'] is not None:
                try:
                    feature_df = get_derived_features_OP(complete_data_df_OP, ELOP_ER_multi_Features, CUTPOINTS_cli_OP)
                    std_feature_df = standardize_df(feature_df[ELOP_ER_multi.feature_names_in_], ELOP_ER_multi_SCALER)
                    results = predict_ER(ELOP_ER_multi, std_feature_df, RISK_THRESHOLD_multi_OP)
                except Exception as e:
                    print(f"Error in processing with `ELOP_ER_multi`: {e}")
            elif complete_data_df_OP_pre is not None:
                try:
                    feature_df = get_derived_features_OP_pre(complete_data_df_OP_pre, ELOP_ER_premulti_Features, CUTPOINTS_precli_OP)
                    std_feature_df = standardize_df(feature_df[ELOP_ER_premulti.feature_names_in_], ELOP_ER_premulti_SCALER)
                    results = predict_ER(ELOP_ER_premulti, std_feature_df, RISK_THRESHOLD_premulti_OP)
                except Exception as e:
                    print(f"Error in processing with `ELOP_ER_multi`: {e}")
            # elif complete_data_df.loc[0, 'Tumor size'] >= 2.5:
            #     try:
            #         feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_Rad_DL_bFeatures, CUTPOINTS)
            #         std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_Rad_DL_bEstimator.feature_names_in_], ELRFA_ER_cli_Rad_DL_bSCALER)
            #         results = predict_ER(ELRFA_ER_cli_Rad_DL_bEstimator, std_feature_df, RISK_THRESHOLD_cli_Rad_DL_bER)
            #     except:
            #         try:
            #             feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_2DRad_DL_bFeatures, CUTPOINTS)
            #             std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_2DRad_DL_bEstimator.feature_names_in_], ELRFA_ER_cli_2DRad_DL_bSCALER)
            #             results = predict_ER(ELRFA_ER_cli_2DRad_DL_bEstimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_DL_bER)
            #         except:
            #             try:
            #                 feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_Rad_bFeatures, CUTPOINTS)
            #                 std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_Rad_bEstimator.feature_names_in_], ELRFA_ER_cli_Rad_bSCALER)
            #                 results = predict_ER(ELRFA_ER_cli_Rad_bEstimator, std_feature_df, RISK_THRESHOLD_cli_Rad_bER)
            #             except:
            #                 try:
            #                     feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_2DRad_bFeatures, CUTPOINTS)
            #                     std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_2DRad_bEstimator.feature_names_in_], ELRFA_ER_cli_2DRad_bSCALER)
            #                     results = predict_ER(ELRFA_ER_cli_2DRad_bEstimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_bER)
            #                 except:
            #                     raise HTTPException(status_code=400, detail="Failed to use your image features.")
            # else:
            #     try:
            #         feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_Rad_DL_sFeatures, CUTPOINTS)
            #         std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_Rad_DL_sEstimator.feature_names_in_], ELRFA_ER_cli_Rad_DL_sSCALER)
            #         results = predict_ER(ELRFA_ER_cli_Rad_DL_sEstimator, std_feature_df, RISK_THRESHOLD_cli_Rad_DL_sER)
            #     except:
            #         try:
            #             feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_2DRad_DL_sFeatures, CUTPOINTS)
            #             std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_2DRad_DL_sEstimator.feature_names_in_], ELRFA_ER_cli_2DRad_DL_sSCALER)
            #             results = predict_ER(ELRFA_ER_cli_2DRad_DL_sEstimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_DL_sER)
            #         except:
            #             try:
            #                 feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_Rad_sFeatures, CUTPOINTS)
            #                 std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_Rad_sEstimator.feature_names_in_], ELRFA_ER_cli_Rad_sSCALER)
            #                 results = predict_ER(ELRFA_ER_cli_Rad_sEstimator, std_feature_df, RISK_THRESHOLD_cli_Rad_sER)
            #             except:
                            # try:
                            #     feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_2DRad_sFeatures, CUTPOINTS)
                            #     std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_2DRad_sEstimator.feature_names_in_], ELRFA_ER_cli_2DRad_sSCALER)
                            #     results = predict_ER(ELRFA_ER_cli_2DRad_sEstimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_sER)
                            # except:
                            #     raise HTTPException(status_code=400, detail="Failed to use your image features.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
    else:
        if clinical_data_df_OP.loc[0, 'Histologic grade'] is not None:
            feature_df = get_derived_features_OP(clinical_data_df_OP, ELOP_ER_cli_Features, CUTPOINTS_cli_OP)
            std_feature_df = standardize_df(feature_df[ELOP_ER_cli.feature_names_in_], ELOP_ER_cli_SCALER)
            results = predict_ER(ELOP_ER_cli, std_feature_df, RISK_THRESHOLD_cli_OP)
        if clinical_data_df_OP_pre is not None:
            feature_df = get_derived_features_OP_pre(clinical_data_df_OP_pre, ELOP_ER_precli_Features, CUTPOINTS_precli_OP)
            std_feature_df = standardize_df(feature_df[ELOP_ER_precli.feature_names_in_], ELOP_ER_precli_SCALER)
            results = predict_ER(ELOP_ER_precli, std_feature_df, RISK_THRESHOLD_precli_OP)
        # elif clinical_data_df.loc[0, 'Tumor size'] >= 2.5:
        #     feature_df = get_derived_features(clinical_data_df, ELRFA_ER_cli_bFeatures, CUTPOINTS)
        #     std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_bEstimator.feature_names_in_], ELRFA_ER_cli_bSCALER)
        #     results = predict_ER(ELRFA_ER_cli_bEstimator, std_feature_df, RISK_THRESHOLD_cli_OP)
        # else:
        #     feature_df = get_derived_features(clinical_data_df, ELRFA_ER_cli_sFeatures, CUTPOINTS)
        #     std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_sEstimator.feature_names_in_], ELRFA_ER_cli_sSCALER)
        #     results = predict_ER(ELRFA_ER_cli_sEstimator, std_feature_df, RISK_THRESHOLD_cli_sER)
    if results is None:
        raise HTTPException(status_code=500, detail="Failed to generate results due to processing errors.")
    return results

@app.post("/api/overall_survival/submit/case")
async def submit(request: Request):
    form_data = await request.form()
    data_dict = {key: value for key, value in form_data.items() if not isinstance(value, UploadFile)}
    file: UploadFile = form_data.get("file")

    try:
        patient_data = PatientData_Surv(**data_dict)
    except ValidationError as e:
        return HTTPException(status_code=400, detail=f"Validation error: {e.errors()}")
    clinical_data_df = pd.DataFrame([patient_data.dict()])
    
    if file:
        file_contents = await file.read()
        try:
            if file.filename.endswith('.csv'):
                image_features_df = pd.read_csv( BytesIO( file_contents ) ).astype('float')
            elif file.filename.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
                image_features_df = pd.read_excel( BytesIO( file_contents ) ).astype('float')
            else:
                raise HTTPException(status_code=400, detail="Unsupported file format")
            
            complete_data_df = pd.concat([clinical_data_df, image_features_df], axis=1)
            
            try:
                feature_df = get_derived_features(complete_data_df, ELRFA_surv_cli_Rad_DL_Features, CUTPOINTS)
                std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Rad_DL_Estimator.feature_names_in_], ELRFA_surv_cli_Rad_DL_SCALER)
                results = predict_surv(ELRFA_surv_cli_Rad_DL_Estimator, std_feature_df, RISK_THRESHOLD_cli_Rad_DL_surv)
            except:
                try:
                    feature_df = get_derived_features(complete_data_df, ELRFA_surv_cli_2DRad_DL_Features, CUTPOINTS)
                    std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_2DRad_DL_Estimator.feature_names_in_], ELRFA_surv_cli_2DRad_DL_SCALER)
                    results = predict_surv(ELRFA_surv_cli_2DRad_DL_Estimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_DL_surv)
                except:
                    try:
                        feature_df = get_derived_features(complete_data_df, ELRFA_surv_cli_Rad_Features, CUTPOINTS)
                        std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Rad_Estimator.feature_names_in_], ELRFA_surv_cli_Rad_SCALER)
                        results = predict_surv(ELRFA_surv_cli_Rad_Estimator, std_feature_df, RISK_THRESHOLD_cli_Rad_surv)
                    except:
                        try:
                            feature_df = get_derived_features(complete_data_df, ELRFA_surv_cli_2DRad_Features, CUTPOINTS)
                            std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_2DRad_Estimator.feature_names_in_], ELRFA_surv_cli_2DRad_SCALER)
                            results = predict_surv(ELRFA_surv_cli_2DRad_Estimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_surv)
                        except:
                            raise HTTPException(status_code=400, detail="Failed to use your image features.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
    else:
        feature_df = get_derived_features(clinical_data_df, ELRFA_surv_cli_Features, CUTPOINTS)
        std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Estimator.feature_names_in_], ELRFA_surv_cli_SCALER)
        results = predict_surv(ELRFA_surv_cli_Estimator, std_feature_df, RISK_THRESHOLD_cli_surv)
    
    return results

# @app.post("/api/early_recurrence/submit/batch")
# async def submit_batch(file: UploadFile):
#     file_contents = await file.read()
#     try:
#         if file.filename.endswith('.csv'):
#             data_df = pd.read_csv( BytesIO( file_contents ) ).astype('float')
#         elif file.filename.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
#             data_df = pd.read_excel( BytesIO( file_contents ) ).astype('float')
#         else:
#             raise HTTPException(status_code=400, detail="Unsupported file format")
        
        
#         if 'Histologic grade' not in data_df.columns :
#             data_df_pre = data_df
#         else:
#             data_df_post = data_df
        
#         results_pre_df = pd.DataFrame()
#         results_post_df = pd.DataFrame()

#         if 'Histologic grade' not in data_df_pre.columns :
#             try:
#                 feature_df_pre = get_derived_features_OP_pre(data_df_pre, ELOP_ER_premulti_Features, CUTPOINTS_precli_OP)
#                 std_feature_df_pre = standardize_df(feature_df_pre[ELOP_ER_premulti.feature_names_in_], ELOP_ER_premulti_SCALER)
#                 results_pre = predict_ER(ELOP_ER_premulti, std_feature_df_pre, RISK_THRESHOLD_premulti_OP, mode="batch")
#                 results_pre_df = pd.DataFrame(results_pre, index=data_df_pre.index)
#             except:
#                 raise HTTPException(status_code=400, detail="Failed to use your features.")

#         if 'Histologic grade' in data_df_post.columns :
#             try:
#                 feature_df_post = get_derived_features_OP(data_df_post, ELOP_ER_multi_Features, CUTPOINTS_cli_OP)
#                 std_feature_df_post = standardize_df(feature_df_post[ELOP_ER_multi.feature_names_in_], ELOP_ER_multi_SCALER)
#                 results_post = predict_ER(ELOP_ER_multi, std_feature_df_post, RISK_THRESHOLD_multi_OP, mode="batch")
#                 results_post_df = pd.DataFrame(results_post, index=data_df_post.index)
#             except:
#                 raise HTTPException(status_code=400, detail="Failed to use your features.")
#         print("DataFrame:", results_pre_df.head())
#         results_df = pd.concat([results_pre_df, results_post_df]).sort_index()
#         print("Results DataFrame:", results_df.head())
#         excel_file = BytesIO()
#         results_df.to_excel(excel_file, index=False)
#         excel_file.seek(0)
#         response = StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#         response.headers["Content-Disposition"] = "attachment; filename=results.xlsx"
#         print(response.headers) 
    
#         return response
#     except Exception as e:
#         return HTTPException(status_code=500, detail=str(e))

@app.post("/api/early_recurrence/submit/batch")
async def submit_batch(file: UploadFile):
    file_contents = await file.read()
    try:
        # 檢查檔案格式並讀取資料
        if file.filename.endswith('.csv'):
            data_df = pd.read_csv(BytesIO(file_contents)).astype('float')
        elif file.filename.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
            data_df = pd.read_excel(BytesIO(file_contents)).astype('float')
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        # 根據有無 'Histologic grade' 欄位分割資料
        data_df_pre, data_df_post = None, None
        if 'Histologic grade' not in data_df.columns:
            data_df_pre = data_df
        else:
            data_df_post = data_df
        
        # 初始化空的 DataFrame 來存儲結果
        results_pre_df = pd.DataFrame()
        results_post_df = pd.DataFrame()

        # 預處理和分析 pre data
        if data_df_pre is not None:
            try:
                feature_df_pre = get_derived_features_OP_pre(data_df_pre, ELOP_ER_premulti_Features, CUTPOINTS_precli_OP)
                std_feature_df_pre = standardize_df(feature_df_pre[ELOP_ER_premulti.feature_names_in_], ELOP_ER_premulti_SCALER)
                results_pre = predict_ER(ELOP_ER_premulti, std_feature_df_pre, RISK_THRESHOLD_premulti_OP, mode="batch")
                results_pre_df = pd.DataFrame(results_pre, index=data_df_pre.index)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Failed to process pre data: {str(e)}")

        # 預處理和分析 post data
        if data_df_post is not None:
            try:
                feature_df_post = get_derived_features_OP(data_df_post, ELOP_ER_multi_Features, CUTPOINTS_cli_OP)
                std_feature_df_post = standardize_df(feature_df_post[ELOP_ER_multi.feature_names_in_], ELOP_ER_multi_SCALER)
                results_post = predict_ER(ELOP_ER_multi, std_feature_df_post, RISK_THRESHOLD_multi_OP, mode="batch")
                results_post_df = pd.DataFrame(results_post, index=data_df_post.index)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Failed to process post data: {str(e)}")

        # 合併 pre 和 post 的結果，並檢查是否為空
        results_df = pd.concat([results_pre_df, results_post_df]).sort_index()
        if results_df.empty:
            raise HTTPException(status_code=400, detail="No valid results generated after processing.")

        # 寫入 Excel 檔案並回傳
        excel_file = BytesIO()
        results_df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        if excel_file.getbuffer().nbytes == 0:
            raise HTTPException(status_code=500, detail="Failed to generate Excel file.")
        
        response = StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = "attachment; filename=results.xlsx"
        print("Response headers:", response.headers)  # Debugging line
        
        return response
    
    except Exception as e:
        print("Exception encountered:", str(e))  # Debugging line
        return HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@app.post("/api/overall_survival/submit/batch")
async def submit_batch(file: UploadFile):
    file_contents = await file.read()
    try:
        if file.filename.endswith('.csv'):
            data_df = pd.read_csv( BytesIO( file_contents ) ).astype('float')
        elif file.filename.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
            data_df = pd.read_excel( BytesIO( file_contents ) ).astype('float')
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        try:
            feature_df = get_derived_features(data_df, ELRFA_surv_cli_Rad_DL_Features, CUTPOINTS)
            std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Rad_DL_Estimator.feature_names_in_], ELRFA_surv_cli_Rad_DL_SCALER)
            results = predict_surv(ELRFA_surv_cli_Rad_DL_Estimator, std_feature_df, RISK_THRESHOLD_cli_Rad_DL_surv, mode="batch")
        except:
            try:
                feature_df = get_derived_features(data_df, ELRFA_surv_cli_2DRad_DL_Features, CUTPOINTS)
                std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_2DRad_DL_Estimator.feature_names_in_], ELRFA_surv_cli_2DRad_DL_SCALER)
                results = predict_surv(ELRFA_surv_cli_2DRad_DL_Estimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_DL_surv, mode="batch")
            except:
                try:
                    feature_df = get_derived_features(data_df, ELRFA_surv_cli_Rad_Features, CUTPOINTS)
                    std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Rad_Estimator.feature_names_in_], ELRFA_surv_cli_Rad_SCALER)
                    results = predict_surv(ELRFA_surv_cli_Rad_Estimator, std_feature_df, RISK_THRESHOLD_cli_Rad_surv, mode="batch")
                except:
                    try:
                        feature_df = get_derived_features(data_df, ELRFA_surv_cli_2DRad_Features, CUTPOINTS)
                        std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_2DRad_Estimator.feature_names_in_], ELRFA_surv_cli_2DRad_SCALER)
                        results = predict_surv(ELRFA_surv_cli_2DRad_Estimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_surv, mode="batch")
                    except:
                        try:
                            feature_df = get_derived_features(data_df, ELRFA_surv_cli_Features, CUTPOINTS)
                            std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Estimator.feature_names_in_], ELRFA_surv_cli_SCALER)
                            results = predict_surv(ELRFA_surv_cli_Estimator, std_feature_df, RISK_THRESHOLD_cli_surv, mode="batch")
                        except:
                            raise HTTPException(status_code=400, detail="Failed to use your features.")
        
        results_df = pd.DataFrame(results)
        excel_file = BytesIO()
        results_df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        response = StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = "attachment; filename=results.xlsx"

        return response
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))