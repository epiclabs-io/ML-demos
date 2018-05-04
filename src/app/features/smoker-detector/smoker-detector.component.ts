import { Component, OnInit } from '@angular/core';
import { SmokerServiceService } from '@app/features/smoker-detector/smoker-service.service';

@Component({
  selector: 'app-smoker-detector',
  templateUrl: './smoker-detector.component.html',
  styleUrls: ['./smoker-detector.component.scss']
})
export class SmokerDetectorComponent implements OnInit {

  public youtubeURL: string;
  public warning: boolean;
  constructor(private smokerService: SmokerServiceService) { }
  ngOnInit() {
    this.smokerService.youtubeURL$.subscribe((value: string) => {
      this.youtubeURL = value;
    });
  }

  public exportWarning(warning: boolean) {
    this.warning = warning;
  }

}

