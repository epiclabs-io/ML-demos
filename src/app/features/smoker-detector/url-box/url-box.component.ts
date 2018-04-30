import { Component, OnInit } from '@angular/core';
import {SmokerServiceService} from "@app/features/smoker-detector/smoker-service.service";

@Component({
  selector: 'app-url-box',
  templateUrl: './url-box.component.html',
  styleUrls: ['./url-box.component.scss']
})
export class UrlBoxComponent implements OnInit {
  public youtubeURL: string;
  constructor(private smokerService: SmokerServiceService) { }

  ngOnInit() {
  }

  public onSubmit(): void {
    this.smokerService.postUrl(this.youtubeURL);
    this.youtubeURL = '';
  }

}
