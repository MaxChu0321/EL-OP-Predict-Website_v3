import sys, os
from dotenv import load_dotenv
load_dotenv()

ELRFA_ER_cli_bMODEL = os.getenv("ELRFA_ER_cli_bMODEL")
ELRFA_ER_cli_sMODEL = os.getenv("ELRFA_ER_cli_sMODEL")
ELRFA_ER_cli_2DRad_bMODEL = os.getenv("ELRFA_ER_cli_2DRad_bMODEL")
ELRFA_ER_cli_2DRad_sMODEL = os.getenv("ELRFA_ER_cli_2DRad_sMODEL")
ELRFA_ER_cli_Rad_bMODEL = os.getenv("ELRFA_ER_cli_Rad_bMODEL")
ELRFA_ER_cli_Rad_sMODEL = os.getenv("ELRFA_ER_cli_Rad_sMODEL")
ELRFA_ER_cli_2DRad_DL_bMODEL = os.getenv("ELRFA_ER_cli_2DRad_DL_bMODEL")
ELRFA_ER_cli_2DRad_DL_sMODEL = os.getenv("ELRFA_ER_cli_2DRad_DL_sMODEL")
ELRFA_ER_cli_Rad_DL_bMODEL = os.getenv("ELRFA_ER_cli_Rad_DL_bMODEL")
ELRFA_ER_cli_Rad_DL_sMODEL = os.getenv("ELRFA_ER_cli_Rad_DL_sMODEL")

ELRFA_surv_cli_MODEL = os.getenv("ELRFA_surv_cli_MODEL")
ELRFA_surv_cli_2DRad_MODEL = os.getenv("ELRFA_surv_cli_2DRad_MODEL")
ELRFA_surv_cli_Rad_MODEL = os.getenv("ELRFA_surv_cli_Rad_MODEL")
ELRFA_surv_cli_2DRad_DL_MODEL = os.getenv("ELRFA_surv_cli_2DRad_DL_MODEL")
ELRFA_surv_cli_Rad_DL_MODEL = os.getenv("ELRFA_surv_cli_Rad_DL_MODEL")

if not ELRFA_surv_cli_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli model.")
elif not ELRFA_surv_cli_2DRad_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli_2DRad model.")
elif not ELRFA_surv_cli_Rad_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli_Rad model.")
elif not ELRFA_surv_cli_2DRad_DL_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli_2DRad_DL model.")
elif not ELRFA_surv_cli_Rad_DL_MODEL: raise ValueError("Cannot find the path of ELRFA_surv_cli_Rad_DL model.")
elif not ELRFA_ER_cli_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_b model.")
elif not ELRFA_ER_cli_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_s model.")
elif not ELRFA_ER_cli_2DRad_DL_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_DL_b model.")
elif not ELRFA_ER_cli_2DRad_DL_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_DL_s model.")
elif not ELRFA_ER_cli_2DRad_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_b model.")
elif not ELRFA_ER_cli_2DRad_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_s model.")
elif not ELRFA_ER_cli_Rad_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_b model.")
elif not ELRFA_ER_cli_Rad_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_s model.")
elif not ELRFA_ER_cli_Rad_DL_bMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_DL_b model.")
elif not ELRFA_ER_cli_Rad_DL_sMODEL: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_DL_s model.")


ELRFA_ER_cli_bSCALER = os.getenv("ELRFA_ER_cli_bSCALER")
ELRFA_ER_cli_sSCALER = os.getenv("ELRFA_ER_cli_sSCALER")
ELRFA_ER_cli_2DRad_DL_bSCALER = os.getenv("ELRFA_ER_cli_2DRad_DL_bSCALER")
ELRFA_ER_cli_2DRad_DL_sSCALER = os.getenv("ELRFA_ER_cli_2DRad_DL_sSCALER")
ELRFA_ER_cli_2DRad_bSCALER = os.getenv("ELRFA_ER_cli_2DRad_bSCALER")
ELRFA_ER_cli_2DRad_sSCALER = os.getenv("ELRFA_ER_cli_2DRad_sSCALER")
ELRFA_ER_cli_Rad_bSCALER = os.getenv("ELRFA_ER_cli_Rad_bSCALER")
ELRFA_ER_cli_Rad_sSCALER = os.getenv("ELRFA_ER_cli_Rad_sSCALER")
ELRFA_ER_cli_Rad_DL_bSCALER = os.getenv("ELRFA_ER_cli_Rad_DL_bSCALER")
ELRFA_ER_cli_Rad_DL_sSCALER = os.getenv("ELRFA_ER_cli_Rad_DL_sSCALER")

ELRFA_surv_cli_SCALER = os.getenv("ELRFA_surv_cli_SCALER")
ELRFA_surv_cli_2DRad_SCALER = os.getenv("ELRFA_surv_cli_2DRad_SCALER")
ELRFA_surv_cli_Rad_SCALER = os.getenv("ELRFA_surv_cli_Rad_SCALER")
ELRFA_surv_cli_2DRad_DL_SCALER = os.getenv("ELRFA_surv_cli_2DRad_DL_SCALER")
ELRFA_surv_cli_Rad_DL_SCALER = os.getenv("ELRFA_surv_cli_Rad_DL_SCALER")

if not ELRFA_surv_cli_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli scaler.")
elif not ELRFA_surv_cli_2DRad_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli_2DRad scaler.")
elif not ELRFA_surv_cli_Rad_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli_Rad scaler.")
elif not ELRFA_surv_cli_2DRad_DL_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli_2DRad_DL scaler.")
elif not ELRFA_surv_cli_Rad_DL_SCALER: raise ValueError("Cannot find the path of ELRFA_surv_cli_Rad_DL scaler.")
elif not ELRFA_ER_cli_bSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_b scaler.")
elif not ELRFA_ER_cli_sSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_s scaler.")
elif not ELRFA_ER_cli_2DRad_bSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_b scaler.")
elif not ELRFA_ER_cli_2DRad_sSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_2DRad_s scaler.")
elif not ELRFA_ER_cli_Rad_bSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_b scaler.")
elif not ELRFA_ER_cli_Rad_sSCALER: raise ValueError("Cannot find the path of ELRFA_ER_cli_Rad_s scaler.")
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


RISK_THRESHOLD_cli_bER = -0.10552763819095479
RISK_THRESHOLD_cli_sER = 0.2160804020100502
RISK_THRESHOLD_cli_2DRad_bER = -0.002821322428163446
RISK_THRESHOLD_cli_2DRad_sER = 0.024421451680127725
RISK_THRESHOLD_cli_Rad_bER = 1.063396789517996
RISK_THRESHOLD_cli_Rad_sER = 0.024504033581742513
RISK_THRESHOLD_cli_2DRad_DL_bER = 0.01586591574408625
RISK_THRESHOLD_cli_2DRad_DL_sER = 0.10197497219227383
RISK_THRESHOLD_cli_Rad_DL_bER = -0.025125628140703515
RISK_THRESHOLD_cli_Rad_DL_sER = 0.5678391959798996

RISK_THRESHOLD_cli_surv = 0.004506343261632435
RISK_THRESHOLD_cli_2DRad_surv = -0.028616976050952817
RISK_THRESHOLD_cli_Rad_surv = -0.02863548918946878
RISK_THRESHOLD_cli_2DRad_DL_surv = 0.015621892635744749
RISK_THRESHOLD_cli_Rad_DL_surv = 0.06573073943600524


# Early Recurrence OP
ELOP_ER_cli_MODEL = os.getenv("ELOP_ER_cli_MODEL")
if not ELOP_ER_cli_MODEL: raise ValueError("Cannot find the path of ELOP_ER_cli model.")
ELOP_ER_cli_SCALER = os.getenv("ELOP_ER_cli_SCALER")
if not ELOP_ER_cli_SCALER: raise ValueError("Cannot find the path of ELOP_ER_cli scaler.")

ELOP_ER_precli_MODEL = os.getenv("ELOP_ER_precli_MODEL")
if not ELOP_ER_precli_MODEL: raise ValueError("Cannot find the path of ELOP_ER_precli model.")
ELOP_ER_precli_SCALER = os.getenv("ELOP_ER_precli_SCALER")
if not ELOP_ER_precli_SCALER: raise ValueError("Cannot find the path of ELOP_ER_precli scaler.")

ELOP_ER_multi_MODEL = os.getenv("ELOP_ER_multi_MODEL")
if not ELOP_ER_multi_MODEL: raise ValueError("Cannot find the path of ELOP_ER_multi model.")
ELOP_ER_multi_SCALER = os.getenv("ELOP_ER_multi_SCALER")
if not ELOP_ER_multi_SCALER: raise ValueError("Cannot find the path of ELOP_ER_multi scaler.")

ELOP_ER_premulti_MODEL = os.getenv("ELOP_ER_premulti_MODEL")
if not ELOP_ER_premulti_MODEL: raise ValueError("Cannot find the path of ELOP_ER_premulti model.")
ELOP_ER_premulti_SCALER = os.getenv("ELOP_ER_premulti_SCALER")
if not ELOP_ER_premulti_SCALER: raise ValueError("Cannot find the path of ELOP_ER_premulti scaler.")

CUTPOINTS_precli_OP = {
    'AFP': [float('-inf'), 7, 10, 20, 200 ,400, float('inf')],
}

CUTPOINTS_cli_OP = {
    'Histologic grade': [float('-inf'), 2, 2.5, 3,float('inf')],
    'AFP': [float('-inf'), 7, 10, 20, 200 ,400, float('inf')],
    'Steatosis grade': [float('-inf'),0.001, float('inf')],
}

RISK_THRESHOLD_cli_OP = 0.5
RISK_THRESHOLD_precli_OP = 0.46
RISK_THRESHOLD_multi_OP = 0.55
RISK_THRESHOLD_premulti_OP = 0.54
if __name__ == "__main__":
    print("EL-RFA-MODELs")