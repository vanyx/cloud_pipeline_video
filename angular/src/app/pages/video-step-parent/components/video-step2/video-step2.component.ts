import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-video-step2',
  templateUrl: './video-step2.component.html',
  styleUrls: ['./video-step2.component.scss']
})
export class VideoStep2Component implements OnInit {

  @Output()
  backEmitter = new EventEmitter();

  @Input()
  data: any[] = [];

  jsonOfData: any = {};

  @Input()
  indexOfSelectedFolder = 1;

  videoUrl = "";

  constructor(private httpClient: HttpClient) {}

  ngOnInit() {
    this.createFiles();
    this.loadJsonFile();
  }

  createFiles() {
    const selectedFolder = this.data[this.indexOfSelectedFolder];

    if (selectedFolder && selectedFolder.contents) {
      const videoFile: string | undefined = selectedFolder.contents.find((content: string) => content.endsWith('.mp4'));

      if (videoFile) {
        this.videoUrl = "https://capydatastorage.s3.eu-north-1.amazonaws.com/" + videoFile;
        console.log(this.videoUrl);
      }
    }
  }

  loadJsonFile() {
    const selectedFolder = this.data[this.indexOfSelectedFolder];

    if (selectedFolder && selectedFolder.contents) {
      const jsonFile: string | undefined = selectedFolder.contents.find((content: string) => content.endsWith('.json'));

      if (jsonFile) {
        const jsonFileUrl = "https://capydatastorage.s3.eu-north-1.amazonaws.com/" + jsonFile;

        // Utilise le service HTTP pour récupérer le fichier JSON
        this.httpClient.get(jsonFileUrl).subscribe(
          (data: any) => {
            this.jsonOfData = data;
            if(this.jsonOfData['langage'] == 'fr') this.jsonOfData['langage'] = 'français';
            if(this.jsonOfData['langage'] == 'en') this.jsonOfData['langage'] = 'English';
            if(this.jsonOfData['langage'] == 'es') this.jsonOfData['langage'] = 'Espagnol';

            console.log(this.jsonOfData);

          },
          (error) => {
            console.error('Erreur lors de la récupération du fichier JSON', error);
          }
        );
      }
    }
  }

  goBack() {
    this.backEmitter.emit();
  }
}
