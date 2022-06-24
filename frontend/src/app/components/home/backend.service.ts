import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseApiUrl } from 'src/app/shared/baseApiUrl';
import { Currency } from './Currency';

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private httpClient: HttpClient) { }

  apiURL = new BaseApiUrl();

  getCurrencies(targetUrl: string, filterObj = null): Observable<Currency> {
    if (targetUrl.length === 0 || targetUrl === null) {
      const endpoint = 'currencies/';
      const httpParams = new HttpParams()
        .append('query', filterObj.query.toString());
      targetUrl = `${this.apiURL.url}${endpoint}`;
      return this.httpClient.get<Currency>(targetUrl, { params: httpParams });
    }
    return this.httpClient.get<Currency>(targetUrl);
  }
  getCurrency(id: number): Observable<Currency> {
    const endpoint = 'currencies/';
    return this.httpClient.get<Currency>(`${this.apiURL.url}${endpoint}${id}/`);
  }
  getCurrencyPrice(dc: string, vs: string): Observable<Currency> {

    const httpParams = new HttpParams()
      .append('dc', dc)
      .append('vs', vs);
    const endpoint = 'currency-prices/';
    const targetUrl = `${this.apiURL.url}${endpoint}`;
    return this.httpClient.get<Currency>(targetUrl, { params: httpParams });
  }



}
