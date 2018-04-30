import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SmokerDetectorComponent } from './smoker-detector.component';

describe('SmokerDetectorComponent', () => {
  let component: SmokerDetectorComponent;
  let fixture: ComponentFixture<SmokerDetectorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SmokerDetectorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SmokerDetectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
