import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoStepParentComponent } from './video-step-parent.component';

describe('VideoStepParentComponent', () => {
  let component: VideoStepParentComponent;
  let fixture: ComponentFixture<VideoStepParentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VideoStepParentComponent]
    });
    fixture = TestBed.createComponent(VideoStepParentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
