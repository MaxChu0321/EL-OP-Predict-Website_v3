import sys, os
from dotenv import load_dotenv
load_dotenv()

ELRFA_ER_cli_bMODEL = os.getenv("ELRFA_ER_cli_bMODEL")
ELRFA_ER_cli_sMODEL = os.getenv("ELRFA_ER_cli_sMODEL")
ELRFA_ER_cli_2DRad_DL_bMODEL = os.getenv("ELRFA_ER_cli_2DRad_DL_bMODEL")
ELRFA_ER_cli_2DRad_DL_sMODEL = os.getenv("ELRFA_ER_cli_2DRad_DL_sMODEL")
ELRFA_ER_cli_Rad_DL_bMODEL = os.getenv("ELRFA_ER_cli_Rad_DL_bMODEL")
ELRFA_ER_cli_Rad_DL_sMODEL = os.getenv("ELRFA_ER_cli_Rad_DL_sMODEL")

ELRFA_surv_cli_MODEL = os.getenv("ELRFA_surv_cli_MODEL")
ELRFA_surv_cli_2DRad_DL_MODEL = os.getenv("ELRFA_surv_cli_2DRad_DL_MODEL")
ELRFA_surv_cli_Rad_DL_MODEL = os.getenv("ELRFA_surv_cli_Rad_DL_MODEL")

if not ELRFA_surv_cli_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli model.")
elif not ELRFA_surv_cli_2DRad_DL_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli_2DRad_DL model.")
elif not ELRFA_surv_cli_Rad_DL_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli_Rad_DL model.")
elif not ELRFA_ER_cli_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_b model.")
elif not ELRFA_ER_cli_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_s model.")
elif not ELRFA_ER_cli_2DRad_DL_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_DL_b model.")
elif not ELRFA_ER_cli_2DRad_DL_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_DL_s model.")
elif not ELRFA_ER_cli_Rad_DL_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_DL_b model.")
elif not ELRFA_ER_cli_Rad_DL_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_DL_s model.")


ELRFA_ER_cli_bSCALER = os.getenv("ELRFA_ER_cli_bSCALER")
ELRFA_ER_cli_sSCALER = os.getenv("ELRFA_ER_cli_sSCALER")
ELRFA_ER_cli_2DRad_DL_bSCALER = os.getenv("ELRFA_ER_cli_2DRad_DL_bSCALER")
ELRFA_ER_cli_2DRad_DL_sSCALER = os.getenv("ELRFA_ER_cli_2DRad_DL_sSCALER")
ELRFA_ER_cli_Rad_DL_bSCALER = os.getenv("ELRFA_ER_cli_Rad_DL_bSCALER")
ELRFA_ER_cli_Rad_DL_sSCALER = os.getenv("ELRFA_ER_cli_Rad_DL_sSCALER")

ELRFA_surv_cli_SCALER = os.getenv("ELRFA_surv_cli_SCALER")
ELRFA_surv_cli_2DRad_DL_SCALER = os.getenv("ELRFA_surv_cli_2DRad_DL_SCALER")
ELRFA_surv_cli_Rad_DL_SCALER = os.getenv("ELRFA_surv_cli_Rad_DL_SCALER")

if not ELRFA_surv_cli_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli scaler.")
elif not ELRFA_surv_cli_2DRad_DL_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli_2DRad_DL scaler.")
elif not ELRFA_surv_cli_Rad_DL_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli_Rad_DL scaler.")
elif not ELRFA_ER_cli_bSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_b scaler.")
elif not ELRFA_ER_cli_sSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_s scaler.")
elif not ELRFA_ER_cli_2DRad_DL_bSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_DL_b scaler.")
elif not ELRFA_ER_cli_2DRad_DL_sSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_DL_s scaler.")
elif not ELRFA_ER_cli_Rad_DL_bSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_DL_b scaler.")
elif not ELRFA_ER_cli_Rad_DL_sSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_DL_s scaler.")


CUTPOINTS = {
    'PTINR': [0, 1.1, float('inf')],  # class_INR
    'BILI': [0, 1.2, 2, float('inf')],  # class_TB
    'Age': [0, 50, 60, 65, float('inf')],
    'Tumor size': [0, 2, 3, 4, 5, 10, float('inf')],
    'CR': [0, 1.2, float('inf')],
    'AFP': [0, 7, 10, 20, 200, 400, float('inf')],
    'BMI': [0, 23, 25, 27, 27.5, 30, float('inf')],
    'Tumor number': [0, 1, float('inf')],
    'ALBIscore': [float('-inf'), -2.60, -1.39, float('inf')],
    'FIB4': [0, 3.25, float('inf')],
    'NLR': [0, 2.5, 3, 4, 5, float('inf')]
}


RISK_THRESHOLD_cli_bER = -0.02196016331913083
RISK_THRESHOLD_cli_sER = -0.00822186254456881
RISK_THRESHOLD_cli_2DRad_DL_bER = 0.01586591574408625
RISK_THRESHOLD_cli_2DRad_DL_sER = 0.10197497219227383
RISK_THRESHOLD_cli_Rad_DL_bER = 1.2038208848145486
RISK_THRESHOLD_cli_Rad_DL_sER = -0.054385421205724295

RISK_THRESHOLD_cli_surv = 0.004506343261632435
RISK_THRESHOLD_cli_2DRad_DL_surv = 0.015621892635744749
RISK_THRESHOLD_cli_Rad_DL_surv = 0.06573073943600524


if __name__ == "__main__":
    print("EL-RFA-MODELs")