import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-score-bar',
  templateUrl: './score-bar.component.html',
  styleUrls: ['./score-bar.component.scss']
})

export class ScoreBarComponent implements OnInit {
  public score: number;
  public tag: string;
  constructor() { }

  @Input()
  set setScore(score: number) {
    this.score = score;
  }

  @Input()
  set setTag(tag: string) {
    this.tag = tag;
  }

  ngOnInit() {
  }

}
