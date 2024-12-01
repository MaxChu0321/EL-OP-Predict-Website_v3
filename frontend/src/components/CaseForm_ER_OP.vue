<template>
  <q-form @submit.prevent="submitForm" class="q-gutter-md custom-bg">
    
    <div class="row q-gutter-md">
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.1" v-model="form.tumor_size" label=" Tumor size (cm)" 
        :rules="[val => (val >= 0 && val <= 10) || 'Value must be between 0 and 10']"/>
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="1" v-model="form.tumor_number" label=" Tumor number" 
        :rules="[val => Number.isInteger(Number(val)) || 'Value must be an integer']"/>
        <!-- <q-input outlined color="indigo-9" type="number" step="0.01" v-model="form.bmi" label="BMI" /> -->
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.height" label=" Height (cm)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.weight" label=" Weight (kg)" />
        
    </div>
    <div class="row q-gutter-md">
        <!-- <q-input outlined color="indigo-9" type="number" step="1" v-model="form.steatosis_grade" label="Steatosis grade" /> -->
        
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="1" v-model="form.ast" label=" AST (U/L)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="1" v-model="form.afp" label=" AFP (ng/mL)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.bili" label=" Bilirubin (mg/dL)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.alb" label=" Albumin (g/dL)" />
        <!-- <q-input outlined color="indigo-9" type="number" step="1" v-model="form.hbsag" label="HBsAg" /> -->
    </div>
    <div class="row q-gutter-md">
        <q-input class="custom-label-spacing" outlined color="indigo-9" type="number" step="0.1" v-model="form.k" label="K (mmol/L)" />
            
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            BCLC stage
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: 'A', value: 1, color: 'yellow' },
                { label: 'B', value: 2, color: 'orange' },
                { label: 'C', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.bclc"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Steatosis grade
            <q-option-group
                :options="[
                { label: 'None', value: 0, color: 'green' },
                { label: 'Mild', value: 1, color: 'yellow' },
                { label: 'Moderate', value: 2, color: 'orange' },
                { label: 'Severe', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.steatosis_grade"
            />
            </div>
            </div>
            <div class="row q-gutter-md">
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Microvascular invasion
            <q-option-group
                :options="[
                { label: 'Absence', value: 0, color: 'green' },
                { label: 'Presence', value: 1, color: 'red' }
                ]"
                type="radio"
                inline
                v-model="form.mvi"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            HBsAg
            <q-option-group
                :options="[
                { label: 'Negative', value: 0, color: 'green' },
                { label: 'Positive', value: 1, color: 'red' }
                ]"
                type="radio"
                inline
                v-model="form.hbsag"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Histologic grade
            <q-option-group
                :options="[
                { label: '1', value: 1, color: 'green' },
                { label: '2', value: 2, color: 'yellow' },
                { label: '3', value: 3, color: 'orange' },
                { label: '4', value: 4, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.histologic_grade"
            />
            </div>
            
            </div>
            <div class="row q-gutter-md">
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Ishak fibrosis stage
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'yellow' },
                { label: '2', value: 2, color: 'yellow' },
                { label: '3', value: 3, color: 'orange' },
                { label: '4', value: 4, color: 'orange' },
                { label: '5', value: 5, color: 'red' },
                { label: '6', value: 6, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.ishak"
            />
            </div>
          </div>
    
    

    <!-- 文件上傳部分 -->
    <div class="row q-gutter-sm">
        <q-file
          v-model="file"
          filled
          label="Upload image features"
          accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
          hint="Accepted files: .csv, .xls, .xlsx"
          color="indigo-9"
          @remove="file = null"
        >
          <template v-slot:prepend>
            <q-icon name="attach_file" />
          </template>
          <template v-slot:append v-if="file">
            <q-btn flat round dense icon="close" color="negative" @click="file = null" />
          </template>
        </q-file>
    </div>

    <!-- Confirmation Dialog for Clearing the Form -->
    <q-dialog v-model="isClearConfirmOpen">
        <q-card>
          <q-card-section>
            Are you sure you want to clear all data from the form?
          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Cancel" color="primary" v-close-popup></q-btn>
            <q-btn flat label="Clear" color="negative" @click="clearForm" v-close-popup></q-btn>
          </q-card-actions>
        </q-card>
    </q-dialog>

    <!-- 提交按钮 -->
    <div class="row q-gutter-md justify-between">
      <div class="col-auto">
        <DownloadExampleButton folderName="OP_ER_Case" />
      </div>
      <div class="col-auto row q-gutter-sm">
        <q-btn unelevated color="red" label="Clear" @click="promptClearForm" />
        <q-btn unelevated color="teal-6" type="button" label="Demo" @click="demo" />
        <q-btn unelevated color="teal-6" type="submit" label="Submit" :loading="submitting">
          <template v-slot:loading>
            <q-spinner-cube color="white" />
          </template>
        </q-btn>
      </div>
    </div>
  </q-form>

  <!-- <q-dialog v-model="isDialogOpen">
    <q-card>
      <q-card-section>
        All fields are required. Please ensure no fields are left blank before submitting.
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="Close" color="primary" v-close-popup></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog> -->
  <q-dialog v-model="isDialogOpen">
    <q-card>
      <q-card-section>
        {{ dialogMessage }}
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="Close" color="primary" v-close-popup></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>

</template>

<script>
import { defineComponent, reactive, ref, computed, toRefs, watch } from 'vue'
import { Notify } from 'quasar'
import { api } from "boot/axios"
import { useJobStore_ER_OP } from 'stores/job'
import { useTestCase_ER_OP } from '../helpers/useDemo'
import DownloadExampleButton from './DownloadExampleButton.vue';

export default defineComponent({
  name: 'CaseForm_ER_OP',
  components: {
    DownloadExampleButton
  },
  emits: ['formSubmitted'],
  props: {
    initialValues: {
      type: Object,
      default: () => ({})
    }
  },
  setup (props, { emit }) {
    const job_store = useJobStore_ER_OP()
    const { initialValues } = toRefs(props)
    let { demo_case } = useTestCase_ER_OP()
    // console.log(demo_case)

    const form = reactive({
      tumor_size: null,
      // lnast: null,
      tumor_number: null,
      ishak: null,
      bmi: null,
      steatosis_grade: null,
      k: null,
      ast: null,
      hbsag: null,
      mvi: null,
      albigrade: null,
      bclc: null,
      histologic_grade: null,
      afp: null,
      height: null,
      weight: null,
      bili: null,
      alb: null,
      // aimorphology_classification: null,
      
    })
    const calculateBMI = () => {
      const heightInMeters = form.height / 100;
      const weightInKg = form.weight;
      form.bmi = heightInMeters > 0 && weightInKg > 0
        ? (weightInKg / (heightInMeters * heightInMeters)).toFixed(2)
        : null;
    };

    const calALBiscore = () => {
      const bilirubin_mg_per_dL = form.bili;
      const albumin_g_per_dL = form.alb;
      const bilirubin_umol_per_L_conversion = 17.1;
      const albumin_g_per_L_conversion = 10;
      const bilirubin_umol_per_L = bilirubin_mg_per_dL * bilirubin_umol_per_L_conversion;
      const albumin_g_per_L = albumin_g_per_dL * albumin_g_per_L_conversion;
      const albi_score = Math.log10(bilirubin_umol_per_L) * 0.66 + albumin_g_per_L * (-0.085)
      if (albi_score <= -2.60) {
          form.albigrade = 1;
        }
      if (albi_score > -2.60 && albi_score <= -1.39) {
          form.albigrade = 2;
        }
      if (albi_score > -1.39) {
          form.albigrade = 3;
        }
    };
    const initForm = () => {
      for (const key in initialValues.value) {
        if (form.hasOwnProperty(key)) {
          form[key] = initialValues.value[key];
        }
      }
    };

    watch( initialValues, () => {
        initForm();
      }, { immediate: true, deep: true }
    );

    initForm();

    const file = ref(null)
    const submitting = ref(false)
    const isDialogOpen = ref(false)
    const dialogMessage = ref("All fields are required. Please ensure no fields are left blank before submitting.");
    const isClearConfirmOpen = ref(false)
    const validationEnabled = ref(true)

    const isFormEmpty = computed(() => {
      return Object.values(form).every(x => x === null || x === '') && file.value === null
    })

    const isFormIncomplete = computed(() => {
      return Object.values(form).some(x => x === null || x === '')  // Checks if any value is null or empty string
    })

    const demo = () => {
      Object.assign(form, demo_case)
    }

    // const demo = () => {
    //   form.tumor_size= demo_case.tumor_size,
    //   // form.lnast= demo_case.lnast,
    //   form.tumor_number= demo_case.tumor_number,
    //   form.ishak= demo_case.ishak,
    //   form.bmi= demo_case.bmi,
    //   form.steatosis_grade= demo_case.steatosis_grade,
    //   form.k= demo_case.k,
    //   form.ast= demo_case.ast,
    //   form.hbsag= demo_case.hbsag,
    //   form.mvi= demo_case.mvi,
    //   form.albigrade= demo_case.albigrade,
    //   form.bclc= demo_case.bclc,
    //   form.histologic_grade= demo_case.histologic_grade,
    //   form.afp= demo_case.afp
    //   form.height= demo_case.height
    //   form.weight= demo_case.weight
    //   form.bili= demo_case.bili
    //   form.alb= demo_case.alb
    //   form.aimorphology_classification= demo_case.aimorphology_classification
    //   // form.steatosis_grade2= demo_case.steatosis_grade2
    // }


    // const submitForm = async () => {
    //   if (isFormIncomplete.value) {
    //     isDialogOpen.value = true  // Open the dialog if form is incomplete
    //     return
    //   }

    //   submitting.value = true
    //   const formData = new FormData()
    //   Object.keys(form).forEach(key => {
    //     formData.append(key, form[key])
    //   })
    //   if (file.value) {
    //     formData.append("file", file.value)
    //   }

    //   try {
    //     const response = await api.post("/early_recurrence/submit/case", formData, {
    //       headers: {
    //         'Accept': 'application/json'
    //       }
    //     })
    //     job_store.updateJobResult(response.data[0])
    //     job_store.updateFormValues(form)
    //     console.log(job_store.risk_score)
    //     emit("formSubmitted", {
    //       formValues: { ...form },
    //       predictionResult: response.data[0],
    //     })
    //     console.log("formSubmitted event emitted with data:", {
    //       formValues: { ...form },
    //       predictionResult: response.data[0],
    //     })
    //   } catch (error) {
    //     console.error("Submission error:", error.message)
    //     const errorMessage = 'Data format error. Please ensure the data is correctly formatted and try again.'
    //     Notify.create({
    //       color: 'negative',
    //       position: 'top',
    //       message: errorMessage,
    //       icon: 'report_problem'
    //     })
    //   } finally {
    //     submitting.value = false
    //   }
    // }
  const submitForm = async () => {
    calculateBMI();
    calALBiscore();
  // 找出為空的欄位
  const emptyFields = Object.keys(form).filter(key => form[key] === null || form[key] === '');

  if (emptyFields.length > 0) {
    // 如果有任何欄位為空，顯示對話框並記錄空欄位名稱
    isDialogOpen.value = true;
    console.log("以下欄位為空，請填寫:", emptyFields); // 在控制台輸出空欄位

    // 在對話框中顯示具體的空欄位
    dialogMessage.value = `請填寫以下欄位: ${emptyFields.join(", ")}`;
    return;
  }

  submitting.value = true;
  const formData = new FormData();
  Object.keys(form).forEach(key => {
    formData.append(key, form[key]);
  });
  if (file.value) {
    formData.append("file", file.value);
  }

  try {
    const response = await api.post("/early_recurrence/submit/case", formData, {
      headers: {
        'Accept': 'application/json'
      }
    });
    job_store.updateJobResult(response.data[0]);
    job_store.updateFormValues(form);
    emit("formSubmitted", {
      formValues: { ...form },
      predictionResult: response.data[0],
    });
  } catch (error) {
    const errorMessage = 'Data format error. Please ensure the data is correctly formatted and try again.';
    Notify.create({
      color: 'negative',
      position: 'top',
      message: errorMessage,
      icon: 'report_problem'
    });
  } finally {
    submitting.value = false;
  }

};


    const promptClearForm = () => {
      if (!isFormEmpty.value) {
        isClearConfirmOpen.value = true
      }
    }

    const clearForm = () => {
      validationEnabled.value = false
      Object.keys(form).forEach(key => {
        form[key] = null
      })
      file.value = null
      setTimeout(() => {
        validationEnabled.value = true
      }, 0)
    }

    return {form, file, submitting, isFormIncomplete, isDialogOpen, isClearConfirmOpen, validationEnabled, submitForm, promptClearForm, clearForm, demo}
  }
})
</script>
<style>
.custom-bg {
  background-color: rgba(255, 255, 255, 0.7); /* 白色背景，50% 透明度 */
}
.custom-label-spacing .q-field__label {
  padding-left: 8px; /* 或任何你需要的間距 */
}
.q-gutter-sm > .q-input {
  margin-top: 2px; /* 設定你想要的間距大小 */
  margin-bottom: 2px; /* 設定你想要的間距大小 */
  margin-left: 8px !important; /* 設定你想要的間距大小 */
  margin-right: 10px !important; /* 設定你想要的間距大小 */
  padding-left: 4px !important; /* 或任何你需要的間距 */
  padding-right: 2px !important; /* 或任何你需要的間距 */
  padding-top: 1px; /* 或任何你需要的間距 */
  padding-bottom: 1px; /* 或任何你需要的間距 */
}
.q-gutter-sm > .q-file {
  margin-top: 2px; /* 設定你想要的間距大小 */
  margin-bottom: 2px; /* 設定你想要的間距大小 */
  margin-left: 2px; /* 設定你想要的間距大小 */
  padding-left: 10px; /* 或任何你需要的間距 */
  padding-right: 14px; /* 或任何你需要的間距 */
  padding-top: 1px; /* 或任何你需要的間距 */
  padding-bottom: 1px; /* 或任何你需要的間距 */
}
.fine-tune {
  margin-left: 12px; /* 設定你想要的間距大小 */
  margin-right: 16px; /* 設定你想要的間距大小 */
}
.q-pa-sm {
  margin-top: 2px; /* 設定你想要的間距大小 */
  margin-bottom: 2px; /* 設定你想要的間距大小 */
  margin-left: 12px; /* 或任何你需要的間距 */
  margin-right: 8px; /* 或任何你需要的間距 */
  padding-top: 1px; /* 或任何你需要的間距 */
  padding-bottom: 1px; /* 或任何你需要的間距 */
}
.no-exclamation {
  display: none;
}
</style>
