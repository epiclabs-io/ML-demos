import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-ad-banner',
  templateUrl: './ad-banner.component.html',
  styleUrls: ['./ad-banner.component.scss']
})

export class AdBannerComponent implements OnInit {
  public url: string;
  public image: string;
  public price: string;
  constructor() { }

  @Input()
  set setUrl(url: string) {
    this.url = url;
  }

  @Input()
  set setImage(image: string) {
    this.image = image;
  }

  @Input()
  set setPrice(price: string) {
    this.price = price;
  }

  ngOnInit() {
  }
}
