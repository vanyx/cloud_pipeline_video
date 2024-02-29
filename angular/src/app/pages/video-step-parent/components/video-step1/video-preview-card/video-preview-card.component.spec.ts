import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoPreviewCardComponent } from './video-preview-card.component';

describe('VideoPreviewCardComponent', () => {
  let component: VideoPreviewCardComponent;
  let fixture: ComponentFixture<VideoPreviewCardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VideoPreviewCardComponent]
    });
    fixture = TestBed.createComponent(VideoPreviewCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
