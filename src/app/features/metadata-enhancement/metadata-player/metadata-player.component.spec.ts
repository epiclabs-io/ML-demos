import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataPlayerComponent } from './metadata-player.component';

describe('MetadataPlayerComponent', () => {
  let component: MetadataPlayerComponent;
  let fixture: ComponentFixture<MetadataPlayerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MetadataPlayerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MetadataPlayerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
