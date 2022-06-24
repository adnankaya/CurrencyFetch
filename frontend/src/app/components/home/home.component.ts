import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BackendService } from './backend.service';
import { Currency } from './Currency';
import { CurrencyPrice } from './CurrencyPrice';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  currencies: Currency[] = [];
  currency_prices: CurrencyPrice[] = [];
  rootUrl = '';
  prevURL = '';
  nextURL = '';
  totalPage = 0;
  totalFound = 0;
  currentPage: number;
  filterObject = {
    limit: 10,
    query: '',
    price: 1
  }
  selectedSortType: string='';
  defaultCurrency:string='';
  targetCurrency:string;
  parity:string='';


  constructor(private backendService: BackendService) { }

  ngOnInit(): void {
    this.getCurrencies(this.rootUrl, this.filterObject)
  }

  getCurrencies(targetURl, filterObj) {
    this.backendService.getCurrencies(targetURl, filterObj).subscribe(
      res => {
        this.currencies = res['results'].map(i => Object.assign(new Currency(), i));
        this.prevURL = res[`previous`];
        this.nextURL = res[`next`];
        this.totalPage = res[`total_pages`];
        this.totalFound = res[`count`];
        this.currentPage = res[`current_page`];
      }, err => {
        throw err;
      }
    );
  }

  getCurrencyParity(defaultCurrency,targetCurrency){
    console.log(this.defaultCurrency, this.targetCurrency);
    
    this.backendService.getCurrencyPrice(defaultCurrency, targetCurrency).subscribe(
      res => {
        this.currency_prices = res['results'].map(i => Object.assign(new CurrencyPrice(), i));
        
      },err => {throw err;}
    );
  }



}
