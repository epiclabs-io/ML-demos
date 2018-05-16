import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AdSummaryComponent } from './ad-summary.component';

describe('AdSummaryComponent', () => {
  let component: AdSummaryComponent;
  let fixture: ComponentFixture<AdSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AdSummaryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AdSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
