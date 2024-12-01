import numpy as np
import pandas as pd
from pydantic import BaseModel, Field
import logging
import joblib
from typing import Type


logger = logging.getLogger(__name__)


def parse_feature(estimator):
    selected_features = estimator.feature_names_in_
    features = dict()
    for feature in selected_features:
        if feature.startswith('class_') or feature.startswith('ln_'):
            details = feature.split("_")
            trans = details[0]
            name = details[1]
        else:
            name = feature
            trans = ""
        
        if name not in features.keys():
            features[name] = [trans]
        else:
            features[name].append(trans)

    return features

def get_derived_features(df, feature_details, cutpoints):
    feature_df = pd.DataFrame()
    for name, transes in feature_details.items():
        for trans in transes:
            if trans == "":
                if name == "Multitumor":
                    feature_df[name] = pd.cut(df['Tumor number'], bins=cutpoints['Tumor number'], labels=list(range( len(cutpoints['Tumor number'])-1 )))
                elif name == "ALBIscore":
                    feature_df[name] = (np.log10(df['BILI'] * 17.1) * 0.66) - ((df['ALB'] * 10) * 0.085)
                elif name == "ALBIgrade":
                    df['ALBIscore'] = (np.log10(df['BILI'] * 17.1) * 0.66) - ((df['ALB'] * 10) * 0.085)
                    feature_df[name] = pd.cut(df['ALBIscore'], bins=cutpoints['ALBIscore'], labels=list(range(1, len(cutpoints['ALBIscore']) )))
                elif name == "APRI":
                    feature_df[name] = (df['AST'] / 45) / (df['PLAT'] / 100000)
                elif name == "BMI":
                    feature_df[name] = df['Weight'] / ((df['Height'] / 100)**2)
                elif name == "NLR":
                    feature_df[name] = df['Neutrophil'] / df['Lymphocyte']
                else:
                    feature_df[name] = df[name]
            elif trans == "class":
                if name == "Size":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['Tumor size'], bins=cutpoints['Tumor size'], labels=list(range( len(cutpoints['Tumor size'])-1 )))
                elif name == "INR":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['PTINR'], bins=cutpoints['PTINR'], labels=list(range( len(cutpoints['PTINR'])-1 )))
                elif name == "TB":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['BILI'], bins=cutpoints['BILI'], labels=list(range( len(cutpoints['BILI'])-1 )))
                elif name == "BMI":
                    df[name] = df['Weight'] / ((df['Height'] / 100)**2)
                    feature_df[f"{trans}_{name}"] = pd.cut(df[name], bins=cutpoints[name], labels=list(range( len(cutpoints[name])-1 )))
                elif name == "NLR":
                    df[name] = df['Neutrophil'] / df['Lymphocyte']
                    feature_df[f"{trans}_{name}"] = pd.cut(df[name], bins=cutpoints[name], labels=list(range( len(cutpoints[name])-1 )))
                elif name == "FIB4":
                    df[name] = (df['Age'] * df['AST']) / ((df['ALT']**0.5) * (df['PLAT'] / 1000))
                    feature_df[f"{trans}_{name}"] = pd.cut(df[name], bins=cutpoints[name], labels=list(range( len(cutpoints[name])-1 )))
                else:
                    feature_df[f"{trans}_{name}"] = pd.cut(df[name], bins=cutpoints[name], labels=list(range( len(cutpoints[name])-1 )))
            elif trans == "ln":
                if name == "BMI":
                    df[name] = df['Weight'] / ((df['Height'] / 100)**2)
                feature_df[f"{trans}_{name}"] = df[name].apply(np.log)

    return feature_df

def standardize_df(df, scaler_pth):
    col_names = df.columns
    scaler = joblib.load(scaler_pth)
    std_data = scaler.transform(df)
    std_feature_df = pd.DataFrame(std_data, columns=col_names)
    
    return std_feature_df


def parse_feature_OP(estimator):
    selected_features = estimator.feature_names_in_
    features = dict()
    for feature in selected_features:
        if "_" not in feature:
            name = feature
            trans = ""
        else:
            details = feature.split("_")
            name = details[1]
            trans = details[0]
        
        if name not in features.keys():
            features[name] = [trans]
        else:
            features[name].append(trans)
    print("Features names:", list(features.keys()))
    print("Features details:", features)

    return features

def get_derived_features_OP(df, feature_details, cutpoints):
    # 打印資料框的欄位名稱，幫助確認欄位的情況
    # print("DataFrame columns:", df.columns.tolist())
    
    feature_df = pd.DataFrame()
    for name, transes in feature_details.items():
        for trans in transes:
            # 檢查欄位是否在資料框中存在
            if name not in df.columns:
                print(f"Warning: Column '{name}' is missing in the input data.")
                continue
            if trans == "":
                feature_df[name] = df[name]
            elif trans == "class":
                if name == "Histologic grade":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['Histologic grade'], bins=cutpoints['Histologic grade'], labels=list(range( len(cutpoints['Histologic grade'])-1 )))
                elif name == "AFP":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['AFP'], bins=cutpoints['AFP'], labels=list(range( len(cutpoints['AFP'])-1 )))
                elif name == "Steatosis grade":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['Steatosis grade'], bins=cutpoints['Steatosis grade'], labels=list(range( len(cutpoints['Steatosis grade'])-1 )))
                # feature_df[f"{trans}_{name}"] = pd.cut(df[name], bins=cutpoints[name], labels=list(range(len(cutpoints[name]) - 1)))
            elif trans == "ln":
                feature_df[f"{trans}_{name}"] = df[name].apply(np.log)
            
        # print("Available columns in df:", feature_df.columns.tolist())
    return feature_df
def get_derived_features_OP_pre(df, feature_details, cutpoints):
    # 打印資料框的欄位名稱，幫助確認欄位的情況
    # print("DataFrame columns:", df.columns.tolist())
    
    feature_df = pd.DataFrame()
    for name, transes in feature_details.items():
        for trans in transes:
            # 檢查欄位是否在資料框中存在
            if name not in df.columns:
                print(f"Warning: Column '{name}' is missing in the input data.")
                continue
            if trans == "":
                feature_df[name] = df[name]
            elif trans == "class":
                if name == "AFP":
                    feature_df[f"{trans}_{name}"] = pd.cut(df['AFP'], bins=cutpoints['AFP'], labels=list(range( len(cutpoints['AFP'])-1 )))
            elif trans == "ln":
                feature_df[f"{trans}_{name}"] = df[name].apply(np.log)
            
        # print("Available columns in df:", feature_df.columns.tolist())
    return feature_df


def predict_ER(estimator, feature_df, RISK_THRESHOLD, mode="case"):
    preds = pd.Series(estimator.predict(feature_df), name='risk_score').round(2)
    risk_groups = preds.apply(lambda risk_score: "High" if risk_score >= RISK_THRESHOLD else "Low" )
    risk_groups.name = 'risk_group'

    survf = estimator.predict_survival_function(feature_df)
    month6_probs = pd.Series(np.asarray([ fn(6) for fn in survf])).round(2)
    month12_probs = pd.Series(np.asarray([ fn(12) for fn in survf])).round(2)
    month18_probs = pd.Series(np.asarray([ fn(18) for fn in survf])).round(2)
    month24_probs = pd.Series(np.asarray([ fn(24) for fn in survf])).round(2)

    results = pd.concat([preds, risk_groups], axis=1).to_dict(orient='records')

    survival_result = pd.concat([month6_probs, month12_probs, month18_probs, month24_probs], axis=1).to_dict(orient='split')['data']

    if mode == "case":
        for idx, result in enumerate(results):
            result['non_recurrence_rates'] = survival_result[idx]  # array
            results[idx] = result
    elif mode == "batch":
        for idx, result in enumerate(results):
            result['6 month Recurrence-free survival rate'] = survival_result[idx][0]
            result['12 month Recurrence-free survival rate'] = survival_result[idx][1]
            result['18 month Recurrence-free survival rate'] = survival_result[idx][2]
            result['24 month Recurrence-free survival rate'] = survival_result[idx][3]
            results[idx] = result

    return results

# def predict_ER(estimator, feature_df, RISK_THRESHOLD, scaler_path=None, mode="case"):
#     # 預測風險分數和風險群體
#     preds = pd.Series(estimator.predict(feature_df), name='risk_score').round(2)
#     risk_groups = preds.apply(lambda risk_score: "High" if risk_score >= RISK_THRESHOLD else "Low")
#     risk_groups.name = 'risk_group'

#     # 計算各個時間點的無復發存活率
#     survf = estimator.predict_survival_function(feature_df)
#     month6_probs = pd.Series(np.asarray([fn(6) for fn in survf])).round(2)
#     month12_probs = pd.Series(np.asarray([fn(12) for fn in survf])).round(2)
#     month18_probs = pd.Series(np.asarray([fn(18) for fn in survf])).round(2)
#     month24_probs = pd.Series(np.asarray([fn(24) for fn in survf])).round(2)

#     # 提取並反正規化 Morphology 欄位值
#     if scaler_path is not None:
#         # 載入包含多個特徵 scaler 的檔案
#         scalers = joblib.load(scaler_path)
        
#         # 確認 'Morphology' 的 scaler 是否存在
#         if 'Morphology' in scalers and 'Morphology' in feature_df.columns:
#             # 提取正規化後的 Morphology 值
#             morphology_normalized = feature_df[['Morphology']].values  # 需要 2D array

#             # 將正規化的值反正規化
#             morphology_original = scalers['Morphology'].inverse_transform(morphology_normalized)

#             # 將反正規化後的數值存入結果
#             morphology_values = pd.Series(morphology_original.flatten(), name="morphology")
#         else:
#             # 如果 'Morphology' 的 scaler 不存在於 scalers 中，或 feature_df 中沒有 Morphology 欄位
#             morphology_values = pd.Series([None] * len(feature_df), name="morphology")
#     else:
#         # 如果沒有提供 scaler_path，則僅提取正規化後的數值（無法反正規化）
#         morphology_values = feature_df.get('Morphology', pd.Series([None] * len(feature_df))).rename("morphology")

#     # 合併結果
#     results = pd.concat([preds, risk_groups, morphology_values], axis=1).to_dict(orient='records')
#     survival_result = pd.concat([month6_probs, month12_probs, month18_probs, month24_probs], axis=1).to_dict(orient='split')['data']

#     # 添加無復發存活率
#     if mode == "case":
#         for idx, result in enumerate(results):
#             result['non_recurrence_rates'] = survival_result[idx]  # array
#             results[idx] = result
#     elif mode == "batch":
#         for idx, result in enumerate(results):
#             result['6 month Recurrence-free survival rate'] = survival_result[idx][0]
#             result['12 month Recurrence-free survival rate'] = survival_result[idx][1]
#             result['18 month Recurrence-free survival rate'] = survival_result[idx][2]
#             result['24 month Recurrence-free survival rate'] = survival_result[idx][3]
#             results[idx] = result

#     return results


# def predict_ER(estimator, feature_df, RISK_THRESHOLD, mode="case"):
#     # 預測風險分數和風險群體
#     preds = pd.Series(estimator.predict(feature_df), name='risk_score').round(2)
#     risk_groups = preds.apply(lambda risk_score: "High" if risk_score >= RISK_THRESHOLD else "Low" )
#     risk_groups.name = 'risk_group'

#     # 計算各個時間點的無復發存活率
#     survf = estimator.predict_survival_function(feature_df)
#     month6_probs = pd.Series(np.asarray([fn(6) for fn in survf])).round(2)
#     month12_probs = pd.Series(np.asarray([fn(12) for fn in survf])).round(2)
#     month18_probs = pd.Series(np.asarray([fn(18) for fn in survf])).round(2)
#     month24_probs = pd.Series(np.asarray([fn(24) for fn in survf])).round(2)

#     # 提取 morphology 欄位的值，假設 morphology 欄位存在於 feature_df 中
#     morphology_values = feature_df.get('Morphology', pd.Series([None] * len(feature_df)))   

#     # 合併結果
#     results = pd.concat([preds, risk_groups, morphology_values.rename("morphology")], axis=1).to_dict(orient='records')
#     print(results)
#     survival_result = pd.concat([month6_probs, month12_probs, month18_probs, month24_probs], axis=1).to_dict(orient='split')['data']

#     if mode == "case":
#         for idx, result in enumerate(results):
#             result['non_recurrence_rates'] = survival_result[idx]  # array
#             results[idx] = result
#     elif mode == "batch":
#         for idx, result in enumerate(results):
#             result['6 month Recurrence-free survival rate'] = survival_result[idx][0]
#             result['12 month Recurrence-free survival rate'] = survival_result[idx][1]
#             result['18 month Recurrence-free survival rate'] = survival_result[idx][2]
#             result['24 month Recurrence-free survival rate'] = survival_result[idx][3]
#             results[idx] = result

#     return results


def predict_surv(estimator, feature_df, RISK_THRESHOLD, mode="case"):
    preds = pd.Series(estimator.predict(feature_df), name='risk_score').round(2)
    risk_groups = preds.apply(lambda risk_score: "High" if risk_score >= RISK_THRESHOLD else "Low" )
    risk_groups.name = 'risk_group'

    survf = estimator.predict_survival_function(feature_df)
    year1_probs = pd.Series(np.asarray([ fn(12) for fn in survf])).round(2)
    year2_probs = pd.Series(np.asarray([ fn(24) for fn in survf])).round(2)
    year3_probs = pd.Series(np.asarray([ fn(36) for fn in survf])).round(2)
    year4_probs = pd.Series(np.asarray([ fn(48) for fn in survf])).round(2)
    year5_probs = pd.Series(np.asarray([ fn(60) for fn in survf])).round(2)
    year6_probs = pd.Series(np.asarray([ fn(72) for fn in survf])).round(2)
    year7_probs = pd.Series(np.asarray([ fn(84) for fn in survf])).round(2)

    results = pd.concat([preds, risk_groups], axis=1).to_dict(orient='records')

    survival_result = pd.concat([year1_probs, year2_probs, year3_probs, year4_probs, year5_probs, year6_probs, year7_probs], axis=1).to_dict(orient='split')['data']

    if mode == "case":
        for idx, result in enumerate(results):
            result['survival_rates'] = survival_result[idx]  # array
            results[idx] = result
    elif mode == "batch":
        for idx, result in enumerate(results):
            result['1 year survival rate'] = survival_result[idx][0]
            result['2 year survival rate'] = survival_result[idx][1]
            result['3 year survival rate'] = survival_result[idx][2]
            result['4 year survival rate'] = survival_result[idx][3]
            result['5 year survival rate'] = survival_result[idx][4]
            result['6 year survival rate'] = survival_result[idx][5]
            result['7 year survival rate'] = survival_result[idx][6]
            results[idx] = result

    return results



if __name__ == "__main__":
    print("test")