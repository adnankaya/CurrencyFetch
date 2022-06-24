export class Calculation {
    // TODO: specify types
    static ceil3Decimal(num: any): any {
        /**
         * Returns given number with 3 Decimal digits
         * as 2 Decimal
         */
        num = parseFloat(num.toFixed(3));
        num = num * 100;
        num = Math.ceil(num);
        num = num / 100;
        return num;
    }
}