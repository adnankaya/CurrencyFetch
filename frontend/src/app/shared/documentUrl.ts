export class DocumentUrl {

    url: string;

    constructor() {
        const baseUrl = location.origin;
        if (baseUrl.indexOf('localhost') > 0) {
            this.url = 'http://localhost:4200/assets/';
        } else {
            this.url = 'http://example.com/www-static/angular/assets/';
        }
    }

}


