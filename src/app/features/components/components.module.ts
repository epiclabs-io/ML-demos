import { NgModule } from '@angular/core';
import { SharedModule } from '@app/shared';
import { ComponentsComponent } from './components.component';
import { TableComponent } from './table/table.component';
import { TableService } from '@app/features/components/table/table.service';
import { AdBannerComponent } from './ad-banner/ad-banner.component';

@NgModule({
  imports: [
    SharedModule,

  ],
  declarations: [
    ComponentsComponent,
    TableComponent,
    AdBannerComponent,
  ],

  providers: [
    TableService,
  ]
})
export class ComponentsModule { }
