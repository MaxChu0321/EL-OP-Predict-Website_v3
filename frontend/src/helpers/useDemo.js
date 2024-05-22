import { ref, reactive, readonly  } from "vue"

// demo 資料為 RFA0534

export function useTestCase_ER(){
  const demo_case = reactive({
    'age': 64,
    'height': 163.3,
    'weight': 70.0,
    'hb': 13.5,
    'afp': 33.2,
    'alk_p': 107.0,
    'cr': 1.20,
    'neutrophil': 59.1,
    'lymphocyte': 35.0,
    'tumor_size': 3.5,
    'tumor_number': 2,
    'wbc': 4800,
    'plat': 92000,
    'ptinr': 1.21,
    'alb': 3.2,
    'bili': 0.78,
    'child_class': 1,
    'bclc': 2,
    'alt': 52,
    'ast': 55,
    'close_to_1_score': 0,
    'close_to_4_score': 2,
    'close_to_56': 0
  })

  return { demo_case:readonly(demo_case) }
}

export function useTestCase_surv(){
  const demo_case = reactive({
    'age': 64,
    'sex': 1,
    'hb': 13.5,
    'bili': 0.78,
    'alb': 3.2,
    'alk_p': 107.0,
    'bun': 12,
    'bclc': 2,
    'cr': 1.20,
    'neutrophil': 59.1,
    'lymphocyte': 35.0,
    'afp': 33.2,
    'alt': 52,
    'hbsag': 1,
    'plat': 92000,
    'wbc': 4800,
    'child_class': 1,
    'ast': 55,
    'height': 163.3,
    'weight': 70.0,
    'hcv': 0,
    'tumor_size': 3.5
  })

  return { demo_case:readonly(demo_case) }
}
