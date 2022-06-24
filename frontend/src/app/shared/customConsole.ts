export class CustomConsole {
    static customConsoleLog(componentName: string, dataName: string, data: any): void {
        console.log(`%c[${componentName}] ${dataName}:\n`, 'background-color:yellow;color:green;font-weight: bold;font-size:16px', data);
    }
}