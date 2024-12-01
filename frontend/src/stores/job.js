import { defineStore } from 'pinia'

export const useJobStore_ER = defineStore('jobER', {
  state: () => ({
    risk_score: null,
    risk_group: null,
    survival_rates: null,
    formValues: null
  }),

  getters: {
    get1yprob: (state) => { return state.survival_rates[1] },
    get2yprob: (state) => { return state.survival_rates[3] },
  },

  actions: {
    updateJobResult (res) {
      this.risk_score = res.risk_score
      this.risk_group = res.risk_group
      this.survival_rates = res.non_recurrence_rates
    },
    updateFormValues(form_values) {
      this.formValues = form_values;
    },
  }
})


export const useJobStore_Surv = defineStore('jobSurv', {
  state: () => ({
    risk_score: null,
    risk_group: null,
    survival_rates: null,
    formValues: null
  }),

  getters: {
    get5yprob: (state) => { return state.survival_rates[4] },
    get3yprob: (state) => { return state.survival_rates[2] },
  },

  actions: {
    updateJobResult (res) {
      this.risk_score = res.risk_score
      this.risk_group = res.risk_group
      this.survival_rates = res.survival_rates
    },
    updateFormValues(form_values) {
      this.formValues = form_values;
    },
  }
})

export const useJobStore_ER_OP_pre = defineStore('jobER_OP_pre', {
  state: () => ({
    risk_score: null,
    risk_group: null,
    survival_rates: null,
    formValues: null,
  }),

  getters: {
    get2yprob: (state) =>{ return state.survival_rates[3] },
    // get3yprob: (state) =>{ return formValues[2] },
  },

  actions: {
    updateJobResult (res) {
      this.risk_score = res.risk_score
      this.risk_group = res.risk_group
      this.survival_rates = res.non_recurrence_rates
    },
    updateFormValues(form_values) {
      this.formValues = form_values;
    },
  }
})

export const useJobStore_ER_OP = defineStore('jobER_OP', {
  state: () => ({
    risk_score: null,
    risk_group: null,
    survival_rates: null,
    formValues: null,
  }),

  getters: {
    get2yprob: (state) =>{ return state.survival_rates[3] },
    // get3yprob: (state) =>{ return formValues[2] },
  },

  // actions: {
  //   updateJobResult (res) {
  //     this.risk_score = res.risk_score;
  //     this.risk_group = res.risk_group;
  //     this.survival_rates = res.survival_rates;
  //     this.formValues = res;
  //   },
  //   updateOriginalFormValues(formValues) {
  //     this.originalFormValues = formValues;}
  // }
  actions: {
    updateJobResult (res) {
      this.risk_score = res.risk_score
      this.risk_group = res.risk_group
      this.survival_rates = res.non_recurrence_rates
    },
    updateFormValues(form_values) {
      this.formValues = form_values;
    },
  }
})