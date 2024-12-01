<template>
  <q-btn
    label="Download example files"
    color="teal-6"
    unelevated
    @click="downloadFiles"
  />
</template>

<script>
export default {
  name: 'DownloadExampleButton',
  props: {
    folderName: {
      type: String,
      required: true
    },
    files: {
      type: Array,
      default: () => [
        { url: 'OS_Case/Overall Survival_image (include Radiomic) features_example.xlsx', name: 'Overall Survival_image (include Radiomic) features_example.xlsx' },
        { url: 'OS_Case/Overall Survival_image (include Radiomic_Geometric) features_example.xlsx', name: 'Overall Survival_image (include Radiomic_Geometric) features_example.xlsx' },
        { url: 'OS_Case/Overall Survival_image (include Radiomic_Geometric_Latent) features_example.xlsx', name: 'Overall Survival_image (include Radiomic_Geometric_Latent) features_example.xlsx' },
        { url: 'OS_Case/Overall Survival_image (include Radiomic_Latent) features_example.xlsx', name: 'Overall Survival_image (include Radiomic_Latent) features_example.xlsx' },
        { url: 'ER_Case/Early Recurrence_image (include Radiomic) features_example.xlsx', name: 'Early Recurrence_image (include Radiomic) features_example.xlsx' },
        { url: 'ER_Case/Early Recurrence_image (include Radiomic_Geometric) features_example.xlsx', name: 'Early Recurrence_image (include Radiomic_Geometric) features_example.xlsx' },
        { url: 'ER_Case/Early Recurrence_image (include Radiomic_Geometric_Latent) features_example.xlsx', name: 'Early Recurrence_image (include Radiomic_Geometric_Latent) features_example.xlsx' },
        { url: 'ER_Case/Early Recurrence_image (include Radiomic_Latent) features_example.xlsx', name: 'Early Recurrence_image (include Radiomic_Latent) features_example.xlsx' },
        { url: 'OS_Batch/Batch_Overall Survival_(include Clinical) features_example.xlsx', name: 'Batch_Overall Survival_(include Clinical) features_example.xlsx' },
        { url: 'OS_Batch/Batch_Overall Survival_(include Clinical_Radiomic) features_example.xlsx', name: 'Batch_Overall Survival_(include Clinical_Radiomic) features_example.xlsx' },
        { url: 'OS_Batch/Batch_Overall Survival_(include Clinical_Radiomic_Geometric) features_example.xlsx', name: 'Batch_Overall Survival_(include Clinical_Radiomic_Geometric) features_example.xlsx' },
        { url: 'OS_Batch/Batch_Overall Survival_(include Clinical_Radiomic_Geometric_Latent) features_example.xlsx', name: 'Batch_Overall Survival_(include Clinical_Radiomic_Geometric_Latent) features_example.xlsx' },
        { url: 'OS_Batch/Batch_Overall Survival_(include Clinical_Radiomic_Latent) features_example.xlsx', name: 'Batch_Overall Survival_(include Clinical_Radiomic_Latent) features_example.xlsx' },
        { url: 'ER_Batch/Batch_Early Recurrence_(include Clinical) features_example.xlsx', name: 'Batch_Early Recurrence_(include Clinical) features_example.xlsx' },
        { url: 'ER_Batch/Batch_Early Recurrence_(include Clinical_Radiomic) features_example.xlsx', name: 'Batch_Early Recurrence_(include Clinical_Radiomic) features_example.xlsx' },
        { url: 'ER_Batch/Batch_Early Recurrence_(include Clinical_Radiomic_Geometric) features_example.xlsx', name: 'Batch_Early Recurrence_(include Clinical_Radiomic_Geometric) features_example.xlsx' },
        { url: 'ER_Batch/Batch_Early Recurrence_(include Clinical_Radiomic_Geometric_Latent) features_example.xlsx', name: 'Batch_Early Recurrence_(include Clinical_Radiomic_Geometric_Latent) features_example.xlsx' },
        { url: 'ER_Batch/Batch_Early Recurrence_(include Clinical_Radiomic_Latent) features_example.xlsx', name: 'Batch_Early Recurrence_(include Clinical_Radiomic_Latent) features_example.xlsx' },
        { url: 'OP_ER_Case/Early Recurrence_OPimage_multi_features_example.csv', name: 'Early Recurrence_OPimage_multi_features_example.csv' },
        { url: 'preOP_ER_Batch/Early Recurrence_OPimage_premulti_features_Batchexample.csv', name: 'Early Recurrence_OPimage_premulti_features_Batchexample.csv' },
        { url: 'postOP_ER_Batch/Early Recurrence_OPimage_postmulti_features_Batchexample.csv', name: 'Early Recurrence_OPimage_postmulti_features_Batchexample.csv' }
      ]
    }
  },
  setup(props) {
    const downloadFiles = () => {
      const folderName = props.folderName;
      const filesToDownload = props.files.filter(file => file.url.startsWith(folderName));

      filesToDownload.forEach(file => {
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
