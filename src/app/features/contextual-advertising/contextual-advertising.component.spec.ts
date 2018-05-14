import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ContextualAdvertisingComponent } from './contextual-advertising.component';

describe('ContextualAdvertisingComponent', () => {
  let component: ContextualAdvertisingComponent;
  let fixture: ComponentFixture<ContextualAdvertisingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ContextualAdvertisingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContextualAdvertisingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
