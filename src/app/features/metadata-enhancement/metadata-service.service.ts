import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {BehaviorSubject} from 'rxjs/BehaviorSubject';

@Injectable()
export class MetadataServiceService {
  private apiUrl = 'http://localhost:6006/api/v1/';
  public youtubeURL$ = new BehaviorSubject<string>('');
  constructor(private http: HttpClient) { }

  public postUrl (url: string): void {
    this.http.post(this.apiUrl + 'processVideo', {video: url}).subscribe((result: any) => {
      this.youtubeURL$.next('http://localhost:6006/static/videos/' + result + '?' + Date.now());
    });
    return;
  }
}
