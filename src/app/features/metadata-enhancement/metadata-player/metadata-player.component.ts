import {Component, Input, OnInit, ViewChild} from '@angular/core';
import {IScoreTS, MetadataServiceService} from '@app/features/metadata-enhancement/metadata-service.service';

@Component({
  selector: 'app-metadata-player',
  templateUrl: './metadata-player.component.html',
  styleUrls: ['./metadata-player.component.scss']
})

export class MetadataPlayerComponent implements OnInit {
  private _youtubeURL: string;
  private scores: IScoreTS[];
  private closestFrame: IScoreTS;
  private interval: any;
  public score = 0.0;
  public warning = false;
  constructor(private metadataService: MetadataServiceService) { }
  @ViewChild('player') player;
  @Input()
  set youtubeURL(youtubeURL: string) {
    setTimeout( this.loadVideo.bind(this, youtubeURL), 5000);
    this.metadataService.returnClassification();
  }
  get youtubeURL(): string {
    return this._youtubeURL;
  }


  ngOnInit() {
    this.metadataService.scores$.subscribe((value: IScoreTS[]) => {
      this.scores = value;
    });
  }


  private async loadVideo(url: string): Promise<void> {
    this._youtubeURL = url;
    this.player.nativeElement.load();
    await this.player.nativeElement.play();  }
}
