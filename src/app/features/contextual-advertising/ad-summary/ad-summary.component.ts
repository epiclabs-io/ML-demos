import { Component, OnInit } from '@angular/core';
import {ContextualServiceService, IBanner} from '@app/features/contextual-advertising/contextual-service.service';

@Component({
  selector: 'app-ad-summary',
  templateUrl: './ad-summary.component.html',
  styleUrls: ['./ad-summary.component.scss']
})
export class AdSummaryComponent implements OnInit {
  public summary: {};
  public taxonomy: {};
  public objectKeys = Object.keys;
  constructor(private metadataService: ContextualServiceService) { }

  ngOnInit() {
    this.metadataService.getSummary().subscribe((result: IBanner[]) => {
      console.log(result);
    });
  }
}
