import { Component, OnInit } from '@angular/core';
import * as AWS from 'aws-sdk';

@Component({
  selector: 'app-video-step-parent',
  templateUrl: './video-step-parent.component.html',
  styleUrls: ['./video-step-parent.component.scss']
})
export class VideoStepParentComponent implements OnInit {

  s3 = new AWS.S3({
    accessKeyId: 'AKIAQSK4UGYQ6WUW7SE3',
    secretAccessKey: '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',
    region: 'eu-north-1',
  });

  indexOfSelectedFolder = 0;

  step = 1;

  ngOnInit() {
    this.retrieveS3Data();
  }

  handleCardClick(i: number) {
    this.step = 2;
    this.indexOfSelectedFolder = i;
  }

  goBackStep1() {
    this.step = 1;
  }

  data: any[] = [];



  retrieveS3Data() {
    const bucketName = 'capydatastorage';

    this.s3.listObjectsV2({ Bucket: bucketName }, (err, s3Data) => {
      if (err) {
        console.error(err);
      } else {
        // Vérifiez que 'Contents' est défini
        if (s3Data.Contents) {
          s3Data.Contents?.forEach((content) => {
            if (content && content.Key) {
              // Séparez le chemin en segments
              const pathSegments = content.Key.split('/');
              // Si l'élément est un fichier (pas un dossier)
              if (pathSegments.length > 1 && pathSegments[1].length > 0) {
                // Trouvez l'objet dans l'array data
                let currentObject = this.data.find(obj => obj.path === pathSegments[0]);

                if (!currentObject) {
                  currentObject = {
                    path: pathSegments[0],
                    contents: []
                  };
                  this.data.push(currentObject);
                }

                // Ajoutez le contenu à l'objet actuel
                currentObject.contents.push(content.Key);
              }
            }
          });

          console.log(this.data); // Affichez le tableau d'objets final
        } else {
          console.error('La propriété Contents est indéfinie dans les données S3.');
        }
      }
    });
  }
}
