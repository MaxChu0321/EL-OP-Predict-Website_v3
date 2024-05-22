<template>
  <q-form
    @submit="submitForm"
    class="q-gutter-md"
  >
    <div class="row justify-between q-gutter-sm">
      <div class="col-auto row justify-start self-center">
        <q-file color="indigo-9" v-model="file" label="Upload file">
          <template v-slot:prepend>
            <q-icon name="attach_file" />
          </template>
        </q-file>
      </div>
      <div class="col-auto row justify-end self-center q-gutter-sm">
        <div class="col-auto">
          <q-btn
            type="submit"
            label="upload"
            color="teal-6"
            :loading="submitting"
            unelevated
          >
            <template v-slot:loading>
              <q-spinner-cube color="white" />
            </template>
          </q-btn>
        </div>
        <div class="col-auto">
          <DownloadExampleButton />
        </div>
      </div>
    </div>
  </q-form>
</template>

<script>
import { defineComponent, reactive, ref } from 'vue';
import { useRouter } from 'vue-router'
import { useQuasar } from 'quasar'
import { api } from 'boot/axios';
import { downloadBlob } from '../helpers/useUtils'
import DownloadExampleButton from './DownloadExampleButton.vue';

export default defineComponent({
  name: 'BatchForm',
  components: {
    DownloadExampleButton
  },
  setup () {
    const file = ref(null)
    const submitting = ref(false)
    const $q = useQuasar()
    const $router = useRouter()

    const getFormData = () =>{
      if (file.value) {
        const formData = new FormData()
        formData.append("file", file.value)
        return formData
      }
      else {
        return null
      }
    }

    const submitForm = () =>{
      let formData = getFormData()
      if (formData == null) {
        $q.notify({
          message: 'Please select the file.',
          color: 'red-8'
        })
      }
      else {
        api.post("submit/batch", formData, { responseType: 'blob' })
          .then((response)=>{
            // // console.log(JSON.stringify(response.data))
            // jobs_store.updateJobsResult(response.data)
            // // console.log(jobs_store.getJobs)
            // $router.push('/result/batch')

            downloadBlob(response.data, 'results.xlsx')

            $q.notify({
              message: 'Results has been downloaded.',
              color: 'green-6'
            })
          })
          .catch((error)=>{
            console.log(error.message)
          })
      }
    }

    return {file, submitting, submitForm}
  }
})
</script>
