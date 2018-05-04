import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import {IScoreTS} from '@app/features/smoker-detector/smoker-service.service';

@Injectable()
export class MetadataServiceService {
  private apiUrl = 'http://localhost:6006/api/v1/';
  private scores: IScoreTS[] = [];
  public youtubeURL$ = new BehaviorSubject<string>('');
  public scores$ = new BehaviorSubject<IScoreTS[]>([]);
  constructor(private http: HttpClient) { }

  public postUrl (url: string): void {
    this.http.post(this.apiUrl + 'processVideo', {video: url}).subscribe((result: any) => {
      this.youtubeURL$.next('http://localhost:6006/static/videos/' + result + '?' + Date.now());
    });
    return;
  }

  public returnClassification (): void {
    this.http.post(this.apiUrl + 'returnClassification', {}).subscribe((result: IClassificationResponse) => {
      this.scores = this.scores.concat(result.scores);
      this.scores$.next(this.scores);
      if (result.classification) {
        setTimeout(this.returnClassification.bind(this), 250);
      }
    });
  }
}

interface IClassificationResponse {
  classification: boolean;
  scores: IScoreTS[];
}

export interface IScoreTS {
  time: string;
  score: string;
}
