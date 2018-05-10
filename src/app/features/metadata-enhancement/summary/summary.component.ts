import { Component, OnInit } from '@angular/core';
import { ISummary, MetadataServiceService } from '@app/features/metadata-enhancement/metadata-service.service';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss']
})

export class SummaryComponent implements OnInit {
  public summary: {};
  public taxonomy: {};
  public objectKeys = Object.keys;
  constructor(private metadataService: MetadataServiceService) { }

  ngOnInit() {
    this.metadataService.getSummary().subscribe((result: ISummary) => {
      this.summary = result.summary;
      this.taxonomy = result.taxonomy;
    });
  }
}
