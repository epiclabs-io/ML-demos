import { CommonModule } from '@angular/common';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { NgModule, Optional, SkipSelf } from '@angular/core';

import {HeadersInterceptor} from '@app/core/injectables/headers-interceptor';

/** Http interceptor providers in outside-in order */
export const httpInterceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: HeadersInterceptor, multi: true },
];


@NgModule({
  imports: [

    // angular
    CommonModule,
    HttpClientModule,

    // own
  ],
  declarations: [
  ],
  providers: [
    httpInterceptorProviders
  ],
})
export class CoreModule {
  constructor (
    @Optional() @SkipSelf() parentModule: CoreModule
  ) {
    if (parentModule) {
      throw new Error('CoreModule is already loaded. Import only in AppModule');
    }
  }
}
