<template>
  <q-page class="q-pa-md">
    <div class="row justify-center">
      <q-card v-if="!showResults" class="q-pa-md column justify-center" flat bordered>

        <q-tabs v-model="mode" dense class="text-grey-7" active-color="indigo-10" indicator-color="deep-orange-8" align="justify">
          <q-tab name="early recurrence" label="Early recurrence" />
          <q-tab name="overall survival" label="Overall survival" />
        </q-tabs>

        <q-tab-panels v-model="mode" animated>
          <q-tab-panel name="early recurrence">
            <CaseForm_ER @formSubmitted="(data) => handleFormSubmission('early recurrence', data)" />
          </q-tab-panel>
          <q-tab-panel name="overall survival">
            <CaseForm_Surv @formSubmitted="(data) => handleFormSubmission('overall survival', data)" />
          </q-tab-panel>
        </q-tab-panels>
      </q-card>

      <div v-if="showResults" class="flex-container full-width">
        <div class="col" align="center">
          <q-tabs v-model="mode" dense class="text-grey-7" active-color="indigo-10" indicator-color="deep-orange-8" align="justify">
            <q-tab name="early recurrence" label="Early recurrence" />
            <q-tab name="overall survival" label="Overall survival" />
          </q-tabs>

          <q-tab-panels v-model="mode" animated>
            <q-tab-panel name="early recurrence">
              <CaseForm_ER class="form-part" :initial-values="formValues" @formSubmitted="(data) => handleFormSubmission('early recurrence', data)" />
            </q-tab-panel>
            <q-tab-panel name="overall survival">
              <CaseForm_Surv class="form-part" :initial-values="formValues" @formSubmitted="(data) => handleFormSubmission('overall survival', data)" />
            </q-tab-panel>
          </q-tab-panels>
        </div>
        <template v-if="resultMode === 'early recurrence'">
          <CaseResultPage_ER class="result-part" />
        </template>
        <template v-else-if="resultMode === 'overall survival'">
          <CaseResultPage_Surv class="result-part" />
        </template>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue'
import CaseForm_ER from "src/components/CaseForm_ER.vue"
import CaseForm_Surv from 'src/components/CaseForm_Surv.vue'
import CaseResultPage_ER from "src/pages/CaseResultPage_ER.vue"
import CaseResultPage_Surv from 'src/pages/CaseResultPage_Surv.vue'

export default defineComponent({
  name: 'IndexPage',
  components: {
    CaseForm_ER,
    CaseForm_Surv,
    CaseResultPage_ER,
    CaseResultPage_Surv
  },
  setup() {
    const mode = ref('early recurrence')
    const resultMode = ref('')
    const showResults = ref(false)
    const formValues = ref(null)

    const handleFormSubmission = (formMode, data) => {
      if (!data || !data.formValues) {
        console.error('Invalid data received:', data);
        return;
      }

      formValues.value = data.formValues;
      showResults.value = true;
      resultMode.value = formMode;
    }

    return { mode, resultMode, showResults, formValues, handleFormSubmission }
  },
})
</script>
<style>
.flex-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
  width: 100%;
}

.form-part {
  max-width: 100%;
  width: 100%;
  margin-right: -250px; /* 负 margin 使得右侧没有留白 */
  margin-left: -40px; /* 负 margin 使得左侧没有留白 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.result-part {
  width: 65%;
  margin-right: -140px;
  margin-left: -40px;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  transition: width 0.3s;
}

.hide-result {
  width: 0;
  overflow: hidden;
  transition: width 0.3s;
}

.full-width {
  width: 100%;
}

.q-mt-md {
  margin-top: 1rem;
}
</style>
