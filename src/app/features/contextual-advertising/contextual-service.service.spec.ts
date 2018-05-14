import { TestBed, inject } from '@angular/core/testing';

import { ContextualServiceService } from './contextual-service.service';

describe('ContextualServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ContextualServiceService]
    });
  });

  it('should be created', inject([ContextualServiceService], (service: ContextualServiceService) => {
    expect(service).toBeTruthy();
  }));
});
