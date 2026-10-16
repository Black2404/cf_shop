import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { login } from '../models/cf_shop.model';
import { loginResponse } from '../models/cf_shop.model';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private http = inject(HttpClient);
  private apiUrl = 'http://127.0.0.1:8000';
  
  login(loginData: login): Observable<loginResponse> {
    return this.http.post<loginResponse>(`${this.apiUrl}/auth/login`, loginData);
  }
}

