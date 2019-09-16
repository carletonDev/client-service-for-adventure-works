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
import { Product } from './product';
import { SalesOrderHeader } from './salesOrderHeader';


export interface SalesOrderDetail { 
    salesOrderId?: number;
    salesOrderDetailId?: number;
    orderQty?: number;
    productId?: number;
    unitPrice?: number;
    unitPriceDiscount?: number;
    lineTotal?: number;
    rowguid?: string;
    modifiedDate?: Date;
    product?: Product;
    salesOrder?: SalesOrderHeader;
}