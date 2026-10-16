import { Injectable, PLATFORM_ID, inject } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { product } from '../models/cf_shop.model';

@Injectable({
  providedIn: 'root'
})
export class productService {
  private http = inject(HttpClient);
  private platformId = inject(PLATFORM_ID);
  private apiUrl = 'http://127.0.0.1:8000';
  
  product(): Observable<product[]> {
    let headers = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    // Chỉ lấy token từ localStorage khi chạy trên trình duyệt (tránh lỗi SSR)
    if (isPlatformBrowser(this.platformId)) {
      const token = localStorage.getItem('token');
      if (token) {
        headers = headers.set('Authorization', `Bearer ${token}`);
      }
    }

    return this.http.get<product[]>(`${this.apiUrl}/products`, { headers });
  }
}