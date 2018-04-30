import { TestBed, inject } from '@angular/core/testing';

import { MetadataServiceService } from './metadata-service.service';

describe('MetadataServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MetadataServiceService]
    });
  });

  it('should be created', inject([MetadataServiceService], (service: MetadataServiceService) => {
    expect(service).toBeTruthy();
  }));
});
