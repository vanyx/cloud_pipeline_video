import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoStep2Component } from './video-step2.component';

describe('VideoStep2Component', () => {
  let component: VideoStep2Component;
  let fixture: ComponentFixture<VideoStep2Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VideoStep2Component]
    });
    fixture = TestBed.createComponent(VideoStep2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
