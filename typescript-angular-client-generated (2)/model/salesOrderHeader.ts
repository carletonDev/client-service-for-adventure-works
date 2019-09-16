/**
 * AdventureWorksAPI
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: v1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
import { Address } from './address';
import { Customer } from './customer';
import { SalesOrderDetail } from './salesOrderDetail';


export interface SalesOrderHeader { 
    salesOrderId?: number;
    revisionNumber?: number;
    orderDate?: Date;
    dueDate?: Date;
    shipDate?: Date;
    status?: number;
    onlineOrderFlag?: boolean;
    salesOrderNumber?: string;
    purchaseOrderNumber?: string;
    accountNumber?: string;
    customerId?: number;
    shipToAddressId?: number;
    billToAddressId?: number;
    shipMethod?: string;
    creditCardApprovalCode?: string;
    subTotal?: number;
    taxAmt?: number;
    freight?: number;
    totalDue?: number;
    comment?: string;
    rowguid?: string;
    modifiedDate?: Date;
    billToAddress?: Address;
    customer?: Customer;
    shipToAddress?: Address;
    salesOrderDetail?: Array<SalesOrderDetail>;
}
