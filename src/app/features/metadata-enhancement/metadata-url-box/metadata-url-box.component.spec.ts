import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataUrlBoxComponent } from './metadata-url-box.component';

describe('MetadataUrlBoxComponent', () => {
  let component: MetadataUrlBoxComponent;
  let fixture: ComponentFixture<MetadataUrlBoxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MetadataUrlBoxComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MetadataUrlBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
