import { ReviewLog } from "./ReviewLog";
import { ServiceProviderMap } from "./ServiceProviderMap";
import { User } from "./User";

export class Provider{
    id?:number;
    is_individual:boolean;
    created_date:string;
    user: User;
    serviceprovidermap_set: ServiceProviderMap[];
    review_logs: ReviewLog[];
}