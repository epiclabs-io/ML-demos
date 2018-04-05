import { Component, OnInit } from '@angular/core';
import {IQuestionAndAnswers} from '@app/features/home/chat/question-and-answers/question-and-answers.component';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  public inputText = '';
  public questionAndAnswers: IQuestionAndAnswers[] = [];
  constructor() { }

  ngOnInit() {
  }

  public onSubmit(): void {
    this.addQuestion(this.inputText);
    this.inputText = '';
  }

  private addQuestion(question: string) {
    this.questionAndAnswers.push({
      question: question,
      answers: ['testy']
    });
  }
}


