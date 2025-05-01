import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import HomePageView from '../views/HomePageView.vue';
import RegisterView from '../views/RegisterView.vue';
import LoginView from '../views/LoginView.vue';
import ProfileDetailView from '../views/ProfileDetailView.vue';
import UserProfileView from '../views/UserProfileView.vue';
import MatchMeView from '../views/MatchMeView.vue';
import ReportView from '../views/ReportView.vue';
import LogoutView from '../views/LogoutView.vue';
import NewProfileView from '../views/NewProfileView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingView
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
      path: '/logout',
      name: 'Logout',
      component: LogoutView
    },
    { path: '/profiles/:profile_id', 
      name: 'ProfileDetails', 
      component: ProfileDetailView 
    },
    { 
      path: '/users/:user_id', 
      name: 'UserProfile', 
      component: UserProfileView 
    },
    {
      path: '/profiles/new',
      name: 'NewProfile',
      component: NewProfileView
    },

    { 
      path: '/profiles/:profile_id/matches', 
      name: 'MatchMe', 
      component: MatchMeView
    },
    { 
      path: '/profiles/favourites', 
      name: 'Reports', 
      component: ReportView
    }
  ]
})

export default router