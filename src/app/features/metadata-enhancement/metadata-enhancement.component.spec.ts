import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataEnhancementComponent } from './metadata-enhancement.component';

describe('MetadataEnhancementComponent', () => {
  let component: MetadataEnhancementComponent;
  let fixture: ComponentFixture<MetadataEnhancementComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MetadataEnhancementComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MetadataEnhancementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
