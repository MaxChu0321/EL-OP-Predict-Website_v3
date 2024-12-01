from pydantic import BaseModel


ER_cli_features = {
    'age': 'Age',
    'height': 'Height',
    'weight': 'Weight',
    'hb': 'HB',
    'afp': 'AFP',
    'alk_p': 'ALK-P',
    'cr': 'CR',
    'neutrophil': 'Neutrophil',
    'lymphocyte': 'Lymphocyte',
    'tumor_size': 'Tumor size',
    'tumor_number': 'Tumor number',
    'wbc': 'WBC',
    'plat': 'PLAT',
    'ptinr': 'PTINR',
    'alb': 'ALB',
    'bili': 'BILI',
    'child_class': 'Child_Class',
    'bclc': 'BCLC',
    'alt': 'ALT',
    'ast': 'AST',
    'close_to_1_score': 'close_to_1_score',
    'close_to_4_score': 'close_to_4_score',
    'close_to_56': 'close_to_56',
}

class PatientData_ER(BaseModel):
    age: float | None = None
    height: float | None = None
    weight: float | None = None
    hb: float | None = None
    afp: float | None = None
    alk_p: float | None = None
    cr: float | None = None
    neutrophil: float | None = None
    lymphocyte: float | None = None
    tumor_size: float | None = None
    tumor_number: float | None = None
    wbc: float | None = None
    plat: float | None = None
    ptinr: float | None = None
    alb: float | None = None
    bili: float | None = None
    child_class: float | None = None
    bclc: float | None = None
    alt: float | None = None
    ast: float | None = None
    close_to_1_score: float | None = None
    close_to_4_score: float | None = None
    close_to_56: float | None = None

    def dict(self, *args, **kwargs):
        original_dict = super().dict(*args, **kwargs)
        return {ER_cli_features[key]: original_dict[key] for key in original_dict if key in ER_cli_features.keys()}


Surv_cli_features = {
    'age': 'Age',
    'sex': 'Sex',
    'hb': 'HB',
    'bili': 'BILI',
    'alb': 'ALB',
    'alk_p': 'ALK-P',
    'bun': 'BUN',
    'bclc': 'BCLC',
    'cr': 'CR',
    'neutrophil': 'Neutrophil',
    'lymphocyte': 'Lymphocyte',
    'afp': 'AFP',
    'alt': 'ALT',
    'hbsag': 'HBsAg',
    'plat': 'PLAT',
    'wbc': 'WBC',
    'child_class': 'Child_Class',
    'ast': 'AST',
    'height': 'Height',
    'weight': 'Weight',
    'hcv': 'HCV',
    'tumor_size': 'Tumor size',
}

class PatientData_Surv(BaseModel):
    age: float | None = None
    sex: float | None = None
    hb: float | None = None
    bili: float | None = None
    alb: float | None = None
    alk_p: float | None = None
    bun: float | None = None
    bclc: float | None = None
    cr: float | None = None
    neutrophil: float | None = None
    lymphocyte: float | None = None
    afp: float | None = None
    alt: float | None = None
    hbsag: float | None = None
    plat: float | None = None
    wbc: float | None = None
    child_class: float | None = None
    ast: float | None = None
    height: float | None = None
    weight: float | None = None
    hcv: float | None = None
    tumor_size: float | None = None

    def dict(self, *args, **kwargs):
        original_dict = super().dict(*args, **kwargs)
        return {Surv_cli_features[key]: original_dict[key] for key in original_dict if key in Surv_cli_features.keys()}


ER_cli_OP_features = {
    'bclc': 'BCLC',
    'tumor_number': 'Tumor number',
    'tumor_size': 'Tumor size',
    'k': 'K',
    'ast': 'AST',
    'afp': 'AFP',
    'hbsag': 'HBsAg',
    'albigrade': 'ALBIgrade',
    'histologic_grade': 'Histologic grade',
    'ishak': 'Ishak',
    'steatosis_grade': 'Steatosis grade',
    'bmi': 'BMI',
    'mvi': 'MVI',
}


class PatientData_ER_OP(BaseModel):
    bclc: float | None = None
    tumor_number: float | None = None
    tumor_size: float | None = None
    k: float | None = None
    ast: float | None = None
    afp: float | None = None
    hbsag: float | None = None
    albigrade: float | None = None
    histologic_grade: float | None = None
    ishak: float | None = None
    steatosis_grade: float | None = None
    bmi: float | None = None
    mvi: float | None = None
    


    def dict(self, *args, **kwargs):
        original_dict = super().dict(*args, **kwargs)
        return {ER_cli_OP_features[key]: original_dict[key] for key in original_dict if key in ER_cli_OP_features.keys()}


ER_precli_OP_features = {
    'bclc': 'BCLC',
    'tumor_number': 'Tumor number',
    'tumor_size': 'Tumor size',
    'k': 'K',
    'ast': 'AST',
    'afp': 'AFP',
    'hbsag': 'HBsAg',
    'albigrade': 'ALBIgrade',
    'bmi': 'BMI',
}


class PatientData_ER_OP_pre(BaseModel):
    bclc: float | None = None
    tumor_number: float | None = None
    tumor_size: float | None = None
    k: float | None = None
    ast: float | None = None
    afp: float | None = None
    hbsag: float | None = None
    albigrade: float | None = None
    bmi: float | None = None


    def dict(self, *args, **kwargs):
        original_dict = super().dict(*args, **kwargs)
        return {ER_cli_OP_features[key]: original_dict[key] for key in original_dict if key in ER_cli_OP_features.keys()}