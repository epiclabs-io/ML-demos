import { Component, OnInit } from '@angular/core';
import {IQuestionAndAnswers} from '@app/features/home/chat/question-and-answers/question-and-answers.component';
import {ChatService} from '@app/features/home/chat/chat.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  public inputText = '';
  public questionAndAnswers: IQuestionAndAnswers[] = [];
  constructor(private chatService: ChatService) { }

  ngOnInit() {
    this.questionAndAnswers = [];
    this.chatService.questionAndAnswers$.subscribe( (data: IQuestionAndAnswers[]) => {
      this.questionAndAnswers = data;
    });
  }

  public onSubmit(): void {
    this.addQuestion(this.inputText);
    this.inputText = '';
  }

  private addQuestion(question: string) {
    this.chatService.getReply(question);
  }
}


