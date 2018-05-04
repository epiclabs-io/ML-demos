import { Component, OnInit } from '@angular/core';
import { MetadataServiceService } from '@app/features/metadata-enhancement/metadata-service.service';

@Component({
  selector: 'app-metadata-url-box',
  templateUrl: './metadata-url-box.component.html',
  styleUrls: ['./metadata-url-box.component.scss']
})
export class MetadataUrlBoxComponent implements OnInit {
  public youtubeURL: string;
  constructor(private metadataService: MetadataServiceService) { }

  ngOnInit() {
  }

  public onSubmit(): void {
    this.metadataService.postUrl(this.youtubeURL);
    this.youtubeURL = '';
  }
}
