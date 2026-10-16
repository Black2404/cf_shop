import { Component, inject, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { productService } from '../../services/products.service';
import { product } from '../../models/cf_shop.model';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './products.html',
  styleUrls: ['./products.css']
})
export class Products {
  private pService = inject(productService);
  private cdr = inject(ChangeDetectorRef);
  productsList: product[] = [];

  ngOnInit(): void {
    this.loadProduct();
  }

  loadProduct(): void {
    this.pService.product().subscribe({
      next: (response: product[]) => {
        console.log('Tải dữ liệu thành công:', response);
        this.productsList = response;
        this.cdr.detectChanges();
      },
      error: (error: any) => {
        console.error('Lỗi khi tải dữ liệu:', error);
      }
    });
  }
}