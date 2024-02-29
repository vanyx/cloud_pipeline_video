import { Component, EventEmitter, Input, OnChanges, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-video-preview-card',
  templateUrl: './video-preview-card.component.html',
  styleUrls: ['./video-preview-card.component.scss']
})
export class VideoPreviewCardComponent {

  @Input()
  title = "";

  @Input()
  urlMiniature = "";

  @Input()
  length = "";
}
