import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { login } from '../../models/cf_shop.model';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login {
  private router = inject(Router);
  private loginService = inject(LoginService);

  loginData: login = { username: '', password: '' };

  onSubmit(): void {
    this.loginService.login(this.loginData).subscribe({
      next: (response) => {
        console.log('Login successful:', response);
        if (response?.access_token) {
          localStorage.setItem('token', response.access_token);
          this.router.navigate(['/staff']);
        }
      },
      error: (error) => {
        console.error('Login failed:', error);
      }
    });
  }
}
