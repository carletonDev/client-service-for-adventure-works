import { NgModule, ModuleWithProviders, SkipSelf, Optional } from '@angular/core';
import { Configuration } from './configuration';
import { HttpClient } from '@angular/common/http';


import { AddressesService } from './api/addresses.service';
import { CustomerAddressesService } from './api/customerAddresses.service';
import { CustomersService } from './api/customers.service';
import { ErrorLogsService } from './api/errorLogs.service';
import { ProductCategoriesService } from './api/productCategories.service';
import { ProductDescriptionsService } from './api/productDescriptions.service';
import { ProductModelProductDescriptionsService } from './api/productModelProductDescriptions.service';
import { ProductModelsService } from './api/productModels.service';
import { ProductsService } from './api/products.service';
import { SalesOrderDetailsService } from './api/salesOrderDetails.service';
import { SalesOrderHeadersService } from './api/salesOrderHeaders.service';
import { ValuesService } from './api/values.service';

@NgModule({
  imports:      [],
  declarations: [],
  exports:      [],
  providers: [
    AddressesService,
    CustomerAddressesService,
    CustomersService,
    ErrorLogsService,
    ProductCategoriesService,
    ProductDescriptionsService,
    ProductModelProductDescriptionsService,
    ProductModelsService,
    ProductsService,
    SalesOrderDetailsService,
    SalesOrderHeadersService,
    ValuesService ]
})
export class ApiModule {
    public static forRoot(configurationFactory: () => Configuration): ModuleWithProviders {
        return {
            ngModule: ApiModule,
            providers: [ { provide: Configuration, useFactory: configurationFactory } ]
        };
    }

    constructor( @Optional() @SkipSelf() parentModule: ApiModule,
                 @Optional() http: HttpClient) {
        if (parentModule) {
            throw new Error('ApiModule is already loaded. Import in your base AppModule only.');
        }
        if (!http) {
            throw new Error('You need to import the HttpClientModule in your AppModule! \n' +
            'See also https://github.com/angular/angular/issues/20575');
        }
    }
}
