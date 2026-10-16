import { Routes } from '@angular/router';
import { Login } from './pages/login/login';
import { Staff } from './pages/staff/staff';
import { Products } from './pages/products/products'

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: Login },
  { path: 'staff', component: Staff },
  { path: 'product', component: Products }
];