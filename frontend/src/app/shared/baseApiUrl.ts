import { Router } from '@angular/router';
export class BaseApiUrl {

    url: string;

    constructor() {
        const baseUrl = location.origin;
        if (baseUrl.indexOf('localhost') > 0) {
            this.url = 'http://127.0.0.1:8000/api/v1/';
        } else {
            this.url = 'http://127.0.0.1:8000/api/v1/';
        }
    }
}
