import { Component, Output,EventEmitter, Input } from '@angular/core';

@Component({
  selector: 'app-video-step1',
  templateUrl: './video-step1.component.html',
  styleUrls: ['./video-step1.component.scss']
})
export class VideoStep1Component {

  @Output()
  indexCardEmitter = new EventEmitter();

  @Input()
  data: any[] = [];

  handleCardClick(i: number) {
    console.log(i)
    this.indexCardEmitter.emit(i);
  }


}
