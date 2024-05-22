
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'early_recurrence/result/case', component: () => import('pages/CaseResultPage_ER.vue') },
      { path: 'overall_survival/result/case', component: () => import('pages/CaseResultPage_Surv.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
