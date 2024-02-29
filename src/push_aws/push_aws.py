import boto3
from botocore.exceptions import NoCredentialsError
import os
import time

def upload_to_s3(local_file, bucket, s3_folder, s3_file):
    """
    Uploads a file to an S3 bucket and creates a folder if it doesn't exist.

    Parameters:
    - local_file (str): Le chemin local du fichier à téléverser.
    - bucket (str): Le nom du bucket S3.
    - s3_folder (str): Le nom du dossier à créer dans le bucket S3.
    - s3_file (str): Le nom du fichier dans le dossier S3.

    Returns:
    - bool: True si le téléchargement est réussi, False sinon.
    """

    # Créer un client S3
    s3 = boto3.client('s3')

    try:
        # Vérifier si le dossier existe, sinon le créer
        s3.head_object(Bucket=bucket, Key=s3_folder + '/')
    except:
        s3.put_object(Bucket=bucket, Key=s3_folder + '/')

    try:
        # Téléverser le fichier dans le dossier spécifié du bucket
        s3.upload_file(local_file, bucket, s3_folder + '/' + s3_file)
        print(f"Le fichier {s3_file} a été téléversé avec succès dans le dossier {s3_folder} du bucket {bucket}.")
        return True
    except NoCredentialsError:
        print("Les informations d'identification AWS n'ont pas été trouvées.")
        return False
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléversement du fichier : {str(e)}")
        return False


# Spécifier les informations nécessaires
local_video_path = "/app/results/capybara_detection.mp4"
aws_bucket_name = "capydatastorage"
s3_folder_name = "Capybara Family's Day"
s3_video_name = "capybara.mp4"
local_json_path = "/app/results/metadata.json"
s3_json_name = "metadata.json"

#wait for the video to be released
while not os.path.exists("/app/tmp/animalDetect_finish.txt"):
    time.sleep(1)

#delete the file if it exists
os.remove("/app/tmp/animalDetect_finish.txt")

# Appeler la fonction pour téléverser le fichier
upload_to_s3(local_video_path, aws_bucket_name, s3_folder_name, s3_video_name)
upload_to_s3(local_json_path, aws_bucket_name, s3_folder_name, s3_json_name)