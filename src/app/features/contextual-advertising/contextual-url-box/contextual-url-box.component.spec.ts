import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContextualUrlBoxComponent } from './contextual-url-box.component';

describe('ContextualUrlBoxComponent', () => {
  let component: ContextualUrlBoxComponent;
  let fixture: ComponentFixture<ContextualUrlBoxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContextualUrlBoxComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContextualUrlBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
