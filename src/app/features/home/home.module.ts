import { NgModule } from '@angular/core';
import { SharedModule } from '@app/shared/shared.module';

import { HomeComponent } from './home.component';
import { ChatComponent } from './chat/chat.component';
import { QuestionAndAnswersComponent } from './chat/question-and-answers/question-and-answers.component';

@NgModule({
  imports: [
    SharedModule,
  ],
  declarations: [HomeComponent, ChatComponent, QuestionAndAnswersComponent]
})
export class HomeModule { }
