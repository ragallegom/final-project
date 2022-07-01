import Vue from 'vue'
import Router from 'vue-router'

import ListNltk from '@/components/Nltk/ListNltk'
import EditNltk from '@/components/Nltk/EditNltk'
import DeleteNltk from '@/components/Nltk/DeleteNltk'
import NewNltk from '@/components/Nltk/NewNltk'
import IndexNltk from '@/components/Nltk/IndexNltk'
import IdentifyNltk from '@/components/Nltk/IdentifyNltk'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'IndexNltk',
      component: IndexNltk
    },
    {
      path: '/identify',
      name: 'IdentifyNltk',
      component: IdentifyNltk
    },
    {
      path: '/corpus',
      name: 'ListNltk',
      component: ListNltk
    },
    {
      path: '/corpus/new',
      name: 'NewNltk',
      component: NewNltk
    },
    {
      path: '/corpus/:corpusId/edit',
      name: 'EditNltk',
      component: EditNltk
    },
    {
      path: '/corpus/:corpusId/delete',
      name: 'DeleteNltk',
      component: DeleteNltk
    }
  ],
  mode: 'history'
})
