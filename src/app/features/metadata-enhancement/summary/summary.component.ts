import { Component, OnInit } from '@angular/core';
import { ISummary, MetadataServiceService } from '@app/features/metadata-enhancement/metadata-service.service';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss']
})
export class SummaryComponent implements OnInit {
  private summary: ISummary;
  constructor(private metadataService: MetadataServiceService) { }

  ngOnInit() {
    this.metadataService.getSummary().subscribe((result: ISummary) => {
      this.summary = result;
    });
  }

}
