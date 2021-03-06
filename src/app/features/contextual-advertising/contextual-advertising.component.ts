import { Component, OnInit } from '@angular/core';
import { ContextualServiceService, IBanner } from '@app/features/contextual-advertising/contextual-service.service';
import { CloudData } from '@app/features/components/tag-cloud/tag-cloud.interfaces';

@Component({
  selector: 'app-contextual-advertising',
  templateUrl: './contextual-advertising.component.html',
  styleUrls: ['./contextual-advertising.component.scss']
})
export class ContextualAdvertisingComponent implements OnInit {

  constructor(private contextual: ContextualServiceService) { }
  public youtubeURL: string;
  public cloudData: CloudData[] = [];
  public banner: IBanner[];
  public started = false;
  public finished = false;

  ngOnInit() {
    this.contextual.youtubeURL$.subscribe((value: string) => {
      this.youtubeURL = value;
    });
  }

  public exportCloud(data: CloudData[]) {
    this.cloudData = data;
  }

  public exportBanner(banner: IBanner[]) {
    this.banner = banner;
  }

  public exportFinished(finished: boolean) {
    this.finished = finished;
    if (finished) {
      this.youtubeURL = '';
    }
  }

  public exportStarted(started: boolean) {
    this.started = started;
  }
}
