import { Provider } from "@angular/core";

export class ReviewLog {
    id?: number;
    service_request_id: number;
    service_request_description: string;
    punctuality_rating: number;
    proficiency_rating: number;
    etiquettes_rating: number;
    communication_rating: number;
    price_rating: number;
    overall_rating: number;
    review: string;
    review_date: string;
    provider: Provider;
    appointment: number;
}