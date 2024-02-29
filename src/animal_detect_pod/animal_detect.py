import subprocess
import json
from moviepy.editor import VideoFileClip
import shutil
import os
import time

def generate_video_with_audio(video_path, video_detection_path):
    # Commande à exécuter pour générer la vidéo sans audio
    command = [
        "python",
        "/app/yolov5/detect.py",
        "--weights", "/app/yolov5/runs/train/exp/weights/last.pt",
        "--img", "640",
        "--conf", "0.6",
        "--source", f"{video_path}"
    ]
    subprocess.run(command)

    # Chemin vers la vidéo générée
    video_generee_path = "/app/yolov5/runs/detect/exp/capybara_subtitled.mp4"

    # Charger la vidéo générée
    video_generee = VideoFileClip(video_generee_path)

    # Charger la vidéo d'origine
    video_origine = VideoFileClip(video_path)

    # Extraire et ajouter l'audio de la vidéo d'origine à la vidéo générée
    video_generee = video_generee.set_audio(video_origine.audio)

    # Sauvegarder la vidéo finale
    video_generee.write_videofile(video_detection_path)

    # Fermer les clips vidéo
    video_generee.close()
    video_origine.close()

    # Supprimer le dossier et son contenu
    shutil.rmtree("/app/yolov5/runs/detect/exp")

#wait for the video to be released
while not os.path.exists("/app/tmp/subtitle_finish.txt"):
    time.sleep(1)

#delete the file if it exists
os.remove("/app/tmp/subtitle_finish.txt")

video_path = "/app/results/capybara_subtitled.mp4"
video_detection_path = "/app/results/capybara_detection.mp4"
# Appeler la fonction pour générer la vidéo avec l'audio
generate_video_with_audio(video_path, video_detection_path)

# Analyser les logs pour extraire les animaux détectés
log_file_path = "/app/tmp/logs.txt"
detected_animals = set()  # Utiliser un ensemble pour éviter les doublons

with open(log_file_path, "r") as log_file:
    for line in log_file:
        if "chat" in line.lower():
            detected_animals.add("chat")
        if "capybara" in line.lower():
            detected_animals.add("capybara")
        if "leopard" in line.lower():
            detected_animals.add("leopard")

# Créer le contenu du fichier JSON si au moins une des trois espèces est détectée
if detected_animals:
    data = {"animaux": list(detected_animals)}

    json_list = []
    json_file_path = "/app/results/metadata.json"

    with open(json_file_path, "r") as jsf:
        json_list = json.load(jsf)

    json_list.update(data)

    # Write updated JSON data
    with open(json_file_path, "w") as json_file:
        json.dump(json_list, json_file, indent=6, separators=(",", ": "))

# Supprimer le fichier de logs
os.remove("/app/tmp/logs.txt")

with open("/app/tmp/animalDetect_finish.txt", "w") as indicator_file:
    indicator_file.write("AnimalDetect finished.")