import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  public inputText = '';
  public questionAndAnswers: IQuestionAndAnswer[] = [];
  constructor() { }

  ngOnInit() {
  }

  public onSubmit(): void {
    console.log(this.inputText);
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

export interface IQuestionAndAnswer {
  question: string;
  answers: string[];
}
