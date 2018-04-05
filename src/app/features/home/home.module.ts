import { NgModule } from '@angular/core';
import { SharedModule } from '@app/shared/shared.module';

import { HomeComponent } from './home.component';
import { ChatComponent } from './chat/chat.component';

@NgModule({
  imports: [
    SharedModule,
  ],
  declarations: [HomeComponent, ChatComponent]
})
export class HomeModule { }
