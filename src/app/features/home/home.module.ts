import { NgModule } from '@angular/core';
import { SharedModule } from '@app/shared/shared.module';

import { HomeComponent } from './home.component';
import { ChatComponent } from './chat/chat.component';
import { QuestionAndAnswersComponent } from './chat/question-and-answers/question-and-answers.component';
import {ChatService} from '@app/features/home/chat/chat.service';

@NgModule({
  imports: [
    SharedModule,
  ],
  providers: [
    ChatService,
  ],
  declarations: [HomeComponent, ChatComponent, QuestionAndAnswersComponent]
})
export class HomeModule { }
