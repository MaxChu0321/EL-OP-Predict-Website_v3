<template>
  <q-btn
    label="Download the example file"
    color="teal-6"
    unelevated
    @click="downloadExcelFile"
  />
</template>

<script>
export default {
  name: 'DownloadExampleButton',
  props: {
    files: {
      type: Array,
      default: () => [
        { url: '/ER_image_features_example.csv', name: 'ER_image_features_example.csv' },
        { url: '/Surv_image_features_example.csv', name: 'Surv_image_features_example.csv' }
      ]
    }
  },
  setup(props) {
    const downloadFiles = () => {
      props.files.forEach(file => {
        const link = document.createElement('a');
        link.href = file.url;
        link.setAttribute('download', file.name);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      });
    };
    return { downloadFiles };
  }
}
</script>
