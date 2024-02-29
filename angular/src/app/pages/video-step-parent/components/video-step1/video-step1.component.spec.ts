import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoStep1Component } from './video-step1.component';

describe('VideoStep1Component', () => {
  let component: VideoStep1Component;
  let fixture: ComponentFixture<VideoStep1Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VideoStep1Component]
    });
    fixture = TestBed.createComponent(VideoStep1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
