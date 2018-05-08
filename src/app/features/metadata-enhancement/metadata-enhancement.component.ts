import { Component, OnInit } from '@angular/core';
import { MetadataServiceService } from '@app/features/metadata-enhancement/metadata-service.service';
import { CloudData } from 'angular-tag-cloud-module';


@Component({
  selector: 'app-metadata-enhancement',
  templateUrl: './metadata-enhancement.component.html',
  styleUrls: ['./metadata-enhancement.component.scss']
})
export class MetadataEnhancementComponent implements OnInit {

  public youtubeURL: string;
  public cloudData: CloudData[] = [];
  constructor(private metadataService: MetadataServiceService) { }
  ngOnInit() {
    this.metadataService.youtubeURL$.subscribe((value: string) => {
      this.youtubeURL = value;
    });
  }

  public exportCloud(data: CloudData[]) {
    this.cloudData = data;
  }
}
