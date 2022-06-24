import { AuthUser } from "./AuthUser";

export class User extends AuthUser{
    email: string;
    phone: string;
    created_date: string;
}