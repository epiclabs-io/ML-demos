import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContextualPlayerComponent } from './contextual-player.component';

describe('ContextualPlayerComponent', () => {
  let component: ContextualPlayerComponent;
  let fixture: ComponentFixture<ContextualPlayerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContextualPlayerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContextualPlayerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
