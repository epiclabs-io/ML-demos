import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs/Subject';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class MetadataServiceService {
  private apiUrl = 'http://localhost:6006/api/v1/';
  public edlUrl = this.apiUrl + 'editlist.edl';
  private scores: IScoreTS[] = [];
  public youtubeURL$ = new Subject<string>();
  public scores$ = new Subject<IScoreTS[]>();
  constructor(private http: HttpClient) { }

  public postUrl (url: string): void {
    this.scores = [];
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
        setTimeout(this.returnClassification.bind(this), 750);
      }
    });
  }

  public getSummary (): Observable<Object> {
    return this.http.get(this.apiUrl + 'returnSummary');
  }
}

interface IClassificationResponse {
  classification: boolean;
  scores: IScoreTS[];
}

export interface IScoreTS {
  time: string;
  tags: ITags[];
}

export interface ITags {
  text: string;
  weight: number;
}

export interface ISummary {
  taxonomy: {};
  summary: {};
}
