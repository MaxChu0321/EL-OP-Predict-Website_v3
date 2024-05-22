import pandas as pd
from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from io import BytesIO
import joblib
import logging
import json
from setting import *
from scripts import parse_feature, get_derived_features, standardize_df, predict_ER, predict_surv
from models import PatientData_ER, PatientData_Surv

# Initial
## setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
# get root logger
logger = logging.getLogger(__name__)
logger.info("Logging...")

logger.info("Import EL-RFA model...")
ELRFA_ER_cli_sEstimator = joblib.load(ELRFA_ER_cli_sMODEL)
ELRFA_ER_cli_bEstimator = joblib.load(ELRFA_ER_cli_bMODEL)
ELRFA_ER_cli_2DRad_DL_sEstimator = joblib.load(ELRFA_ER_cli_2DRad_DL_sMODEL)
ELRFA_ER_cli_2DRad_DL_bEstimator = joblib.load(ELRFA_ER_cli_2DRad_DL_bMODEL)
ELRFA_ER_cli_Rad_DL_sEstimator = joblib.load(ELRFA_ER_cli_Rad_DL_sMODEL)
ELRFA_ER_cli_Rad_DL_bEstimator = joblib.load(ELRFA_ER_cli_Rad_DL_bMODEL)
ELRFA_surv_cli_Estimator = joblib.load(ELRFA_surv_cli_MODEL)
ELRFA_surv_cli_2DRad_DL_Estimator = joblib.load(ELRFA_surv_cli_2DRad_DL_MODEL)
ELRFA_surv_cli_Rad_DL_Estimator = joblib.load(ELRFA_surv_cli_Rad_DL_MODEL)

logger.info("Get EL-RFA features...")
ELRFA_ER_cli_sFeatures = parse_feature(ELRFA_ER_cli_sEstimator)
ELRFA_ER_cli_bFeatures = parse_feature(ELRFA_ER_cli_bEstimator)
ELRFA_ER_cli_2DRad_DL_sFeatures = parse_feature(ELRFA_ER_cli_2DRad_DL_sEstimator)
ELRFA_ER_cli_2DRad_DL_bFeatures = parse_feature(ELRFA_ER_cli_2DRad_DL_bEstimator)
ELRFA_ER_cli_Rad_DL_sFeatures = parse_feature(ELRFA_ER_cli_Rad_DL_sEstimator)
ELRFA_ER_cli_Rad_DL_bFeatures = parse_feature(ELRFA_ER_cli_Rad_DL_bEstimator)
ELRFA_surv_cli_Features = parse_feature(ELRFA_surv_cli_Estimator)
ELRFA_surv_cli_2DRad_DL_Features = parse_feature(ELRFA_surv_cli_2DRad_DL_Estimator)
ELRFA_surv_cli_Rad_DL_Features = parse_feature(ELRFA_surv_cli_Rad_DL_Estimator)

logger.info("Initial API...")
app = FastAPI()

# CORS
origins = [
    "*"
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
    form_data = await request.form()
    data_dict = {key: value for key, value in form_data.items() if not isinstance(value, UploadFile)}
    file: UploadFile = form_data.get("file")

    try:
        patient_data = PatientData_ER(**data_dict)
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
            
            if complete_data_df.loc[0, 'Tumor size'] >= 2.5:
                try:
                    feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_Rad_DL_bFeatures, CUTPOINTS)
                    std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_Rad_DL_bEstimator.feature_names_in_], ELRFA_ER_cli_Rad_DL_bSCALER)
                    results = predict_ER(ELRFA_ER_cli_Rad_DL_bEstimator, std_feature_df, RISK_THRESHOLD_cli_Rad_DL_bER)
                except:
                    try:
                        feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_2DRad_DL_bFeatures, CUTPOINTS)
                        std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_2DRad_DL_bEstimator.feature_names_in_], ELRFA_ER_cli_2DRad_DL_bSCALER)
                        results = predict_ER(ELRFA_ER_cli_2DRad_DL_bEstimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_DL_bER)
                    except:
                        raise HTTPException(status_code=400, detail="Failed to use your image features.")
            else:
                try:
                    feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_Rad_DL_sFeatures, CUTPOINTS)
                    std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_Rad_DL_sEstimator.feature_names_in_], ELRFA_ER_cli_Rad_DL_sSCALER)
                    results = predict_ER(ELRFA_ER_cli_Rad_DL_sEstimator, std_feature_df, RISK_THRESHOLD_cli_Rad_DL_sER)
                except:
                    try:
                        feature_df = get_derived_features(complete_data_df, ELRFA_ER_cli_2DRad_DL_sFeatures, CUTPOINTS)
                        std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_2DRad_DL_sEstimator.feature_names_in_], ELRFA_ER_cli_2DRad_DL_sSCALER)
                        results = predict_ER(ELRFA_ER_cli_2DRad_DL_sEstimator, std_feature_df, RISK_THRESHOLD_cli_2DRad_DL_sER)
                    except:
                        raise HTTPException(status_code=400, detail="Failed to use your image features.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
    else:
        if clinical_data_df.loc[0, 'Tumor size'] >= 2.5:
            feature_df = get_derived_features(clinical_data_df, ELRFA_ER_cli_bFeatures, CUTPOINTS)
            std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_bEstimator.feature_names_in_], ELRFA_ER_cli_bSCALER)
            results = predict_ER(ELRFA_ER_cli_bEstimator, std_feature_df, RISK_THRESHOLD_cli_bER)
        else:
            feature_df = get_derived_features(clinical_data_df, ELRFA_ER_cli_sFeatures, CUTPOINTS)
            std_feature_df = standardize_df(feature_df[ELRFA_ER_cli_sEstimator.feature_names_in_], ELRFA_ER_cli_sSCALER)
            results = predict_ER(ELRFA_ER_cli_sEstimator, std_feature_df, RISK_THRESHOLD_cli_sER)
    
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
                    raise HTTPException(status_code=400, detail="Failed to use your image features.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
    else:
        feature_df = get_derived_features(clinical_data_df, ELRFA_surv_cli_Features, CUTPOINTS)
        std_feature_df = standardize_df(feature_df[ELRFA_surv_cli_Estimator.feature_names_in_], ELRFA_surv_cli_SCALER)
        results = predict_surv(ELRFA_surv_cli_Estimator, std_feature_df, RISK_THRESHOLD_cli_surv)
    
    return results