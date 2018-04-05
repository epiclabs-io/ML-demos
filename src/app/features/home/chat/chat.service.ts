import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Subject} from 'rxjs/Subject';
import {IQuestionAndAnswers} from '@app/features/home/chat/question-and-answers/question-and-answers.component';
import {BehaviorSubject} from 'rxjs/BehaviorSubject';

@Injectable()
export class ChatService {
  private apiUrl = 'http://192.168.0.68:5001/';  // URL to web api
  public questionAndAnswers$ = new BehaviorSubject<IQuestionAndAnswers[]>([]);
  private questionAndAnswersData: IQuestionAndAnswers[] = [];

  constructor(private http: HttpClient) { }

  public getReply(question: string) {
    const newData: IQuestionAndAnswers = {
      question: question,
      answers: []
    };

    this.questionAndAnswersData.push(newData);
    this.questionAndAnswers$.next(this.questionAndAnswersData);
    this.http.post(this.apiUrl + 'answer', {'message': question}).subscribe((response: any): void => {
      newData.answers = response.answer;
      this.questionAndAnswers$.next(this.questionAndAnswersData);
    });
  }
}

