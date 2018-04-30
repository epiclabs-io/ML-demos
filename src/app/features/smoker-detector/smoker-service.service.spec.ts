import { TestBed, inject } from '@angular/core/testing';

import { SmokerServiceService } from './smoker-service.service';

describe('SmokerServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SmokerServiceService]
    });
  });

  it('should be created', inject([SmokerServiceService], (service: SmokerServiceService) => {
    expect(service).toBeTruthy();
  }));
});
