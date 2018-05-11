import { Component, OnInit } from '@angular/core';
import { MetadataServiceService } from '@app/features/metadata-enhancement/metadata-service.service';
import { CloudData } from '@app/features/components/tag-cloud/tag-cloud.interfaces';

@Component({
  selector: 'app-metadata-enhancement',
  templateUrl: './metadata-enhancement.component.html',
  styleUrls: ['./metadata-enhancement.component.scss']
})
export class MetadataEnhancementComponent implements OnInit {

  constructor(private metadataService: MetadataServiceService) { }
  public youtubeURL: string;
  public cloudData: CloudData[] = [];
  public started = false;
  public finished = false;
  public edlUrl = this.metadataService.edlUrl;

  ngOnInit() {
    this.metadataService.youtubeURL$.subscribe((value: string) => {
      this.youtubeURL = value;
    });
  }

  public exportCloud(data: CloudData[]) {
    this.cloudData = data;
  }

  public exportFinished(finished: boolean) {
    this.finished = finished;
  }

  public exportStarted(started: boolean) {
    this.started = started;
  }
}
