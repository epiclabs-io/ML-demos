import {Component, EventEmitter, Input, OnInit, Output, ViewChild} from '@angular/core';
import {IScoreTS, MetadataServiceService} from '@app/features/metadata-enhancement/metadata-service.service';
import { CloudData, CloudOptions } from '@app/features/components/tag-cloud/tag-cloud.interfaces';

@Component({
  selector: 'app-metadata-player',
  templateUrl: './metadata-player.component.html',
  styleUrls: ['./metadata-player.component.scss']
})

export class MetadataPlayerComponent implements OnInit {
  private _youtubeURL: string;
  private scores: IScoreTS[];
  private closestFrame: IScoreTS;
  private finished = false;
  private interval: any;
  public options: CloudOptions;
  public data: CloudData[] = [];
  constructor(private metadataService: MetadataServiceService) { }
  @ViewChild('player') player;
  @Output() dataExport = new EventEmitter<CloudData[]>();
  @Output() startedExport = new EventEmitter<boolean>();
  @Output() finishedExport = new EventEmitter<boolean>();
  @Input()
  set youtubeURL(youtubeURL: string) {
    setTimeout( this.loadVideo.bind(this, youtubeURL), 45000);
    this.metadataService.returnClassification();
  }

  get youtubeURL(): string {
    return this._youtubeURL;
  }


  ngOnInit() {
    this.metadataService.scores$.subscribe((value: IScoreTS[]) => {
      this.scores = value;
    });
    this.options = {width: 1000, height: 400, overflow: false};
  }

  private async loadVideo(url: string): Promise<void> {
    this._youtubeURL = url;
    this.finished = false;
    this.finishedExport.emit(this.finished);
    this.player.nativeElement.load();
    await this.player.nativeElement.play();
    this.startedExport.emit(true);
    this.interval = setInterval( () => {
      if (!this.player.nativeElement.ended) {
        const time = this.player.nativeElement.currentTime;
        this.closestFrame = this.getClosestFrame(time);
        if (this.closestFrame) {
          console.log(time, this.closestFrame.time);
          this.dataExport.emit(this.closestFrame.tags);
          this.scores.splice(this.scores.indexOf(this.closestFrame), 1);
        }
      } else {
        console.log('Video is finished');
        if (!this.finished) {
          this.finished = true;
          this.finishedExport.emit(this.finished);
          clearInterval(this.interval);
        }
      }
    }, 500);
  }

  private getClosestFrame(playerTime: number): IScoreTS {
    return this.scores.find((score) => {
      return Math.abs(parseFloat(score.time) - playerTime) < 0.25;
    });
  }
}
