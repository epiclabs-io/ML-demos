import {Component, EventEmitter, Input, OnInit, Output, ViewChild} from '@angular/core';
import {IScoreTS, SmokerServiceService} from '@app/features/smoker-detector/smoker-service.service';


@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})

export class PlayerComponent implements OnInit {
  private _youtubeURL: string;
  private scores: IScoreTS[];
  private closestFrame: IScoreTS;
  private interval: any;
  public score = 0.0;
  public warning = false;
  constructor(private smokerService: SmokerServiceService) { }
  @ViewChild('player') player;
  @Output() warningExport = new EventEmitter<boolean>();
  @Input()
  set youtubeURL(youtubeURL: string){
    setTimeout( this.loadVideo.bind(this, youtubeURL), 5000);
    this.smokerService.returnClassification();
  }
  get youtubeURL(): string{
    return this._youtubeURL;
  }


  ngOnInit() {
    this.smokerService.scores$.subscribe((value: IScoreTS[]) => {
      this.scores = value;
    });
  }



  private async loadVideo(url: string): Promise<void> {
    this._youtubeURL = url;
    this.player.nativeElement.load();
    await this.player.nativeElement.play();
    this.interval = setInterval( () => {
      if (!this.player.nativeElement.ended) {
        const time = this.player.nativeElement.currentTime;
        this.closestFrame = this.getClosestFrame(time);
        if (this.closestFrame){
          console.log(time, this.closestFrame.time);
          this.score = 100 * parseFloat(this.closestFrame.score);
          this.warning = this.score > 75.0;
          this.warningExport.emit(this.warning);
        }
      } else {
        clearInterval(this.interval);
      }
    }, 500);
  }

  private getClosestFrame(playerTime: number): IScoreTS {
    return this.scores.find((score) => {
      return Math.abs(parseFloat(score.time) - playerTime) < 0.25;
    });
  }
}

