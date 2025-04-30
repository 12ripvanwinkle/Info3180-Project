import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomePageView from '../views/HomePageView.vue';
import RegisterView from '../views/RegisterView.vue';
import LoginView from '../views/LoginView.vue';
import ProfileDetailView from '../views/ProfileDetailView.vue';
import MyProfileView from '../views/MyProfileView.vue';
import NewProfileView from '../views/NewProfileView.vue';
import FavouritesView from '../views/FavouritesView.vue';
import MatchReportView from '../views/MatchReportView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/home',
      name: 'homepage',
      component: HomePageView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/users/{user_id}',
      name: 'my profile',
      component: MyProfileView
    },
    {
      path: '/profiles/new',
      name: 'new profile',
      component: NewProfileView
    },
    {
      path: '/profiles/{profile_id}',
      name: 'profile detail',
      component: ProfileDetailView
    },
    {
      path: '//profiles/favourites',
      name: 'favourite',
      component: FavouritesView
    }
  ]
})

export default router