import { Provider } from "@angular/core";
import { Service } from "../service/Service";

export class ServiceProviderMap{
    id?: number;
    service_offering_description: string;
    experience_in_months: number;
    billing_rate_per_hour: string; 
    service: Service;
    provider: Provider;
}