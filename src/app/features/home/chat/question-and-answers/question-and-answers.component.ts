import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-question-and-answers',
  templateUrl: './question-and-answers.component.html',
  styleUrls: ['./question-and-answers.component.scss']
})
export class QuestionAndAnswersComponent implements OnInit {
  @Input() questionAndAnswers: IQuestionAndAnswers;
  constructor() { }

  ngOnInit() {
  }

}

export interface IQuestionAndAnswers {
  question: string;
  answers: string[];
}
