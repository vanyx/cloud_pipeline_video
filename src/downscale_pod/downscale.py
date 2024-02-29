import moviepy.editor as mp


class DownscalePod:
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path
        self.video = mp.VideoFileClip(self.video_path)
    
    def downscale(self, height: int, filename: str) -> None:
        clip_resized = self.video.resize(height=height)
        clip_resized.write_videofile(filename)
        with open("/app/tmp/downscale_finish.txt", "w") as indicator_file:
            indicator_file.write("Downscale finished.")

video_path = "/app/ressources/capybara.mp4"
video_path_resized = "/app/results/capybara_resized.mp4"
downpod1 = DownscalePod(video_path)
downpod1.downscale(360, video_path_resized)

