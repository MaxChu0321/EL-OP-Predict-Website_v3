
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/CataloguePage.vue') },
      { path: 'early_recurrence', component: () => import('pages/IndexPage_ER.vue') },
      { path: 'overall_survival', component: () => import('pages/IndexPage_Surv.vue') },
      { path: 'OP_early_recurrence_pre', component: () => import('pages/IndexPage_ER_OP_pre.vue') },
      { path: 'OP_early_recurrence', component: () => import('pages/IndexPage_ER_OP.vue') }
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
