import { Component, OnInit } from '@angular/core';
import { ContextualServiceService } from '@app/features/contextual-advertising/contextual-service.service';

@Component({
  selector: 'app-contextual-url-box',
  templateUrl: './contextual-url-box.component.html',
  styleUrls: ['./contextual-url-box.component.scss']
})
export class ContextualUrlBoxComponent implements OnInit {
  public youtubeURL: string;
  constructor(private contextualService: ContextualServiceService) { }

  ngOnInit() {
  }

  public onSubmit(): void {
    this.contextualService.postUrl(this.youtubeURL);
    this.youtubeURL = '';
  }
}
