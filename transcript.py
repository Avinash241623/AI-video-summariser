from youtube_transcript_api import YouTubeTranscriptApi
import whisper
from moviepy.editor import VideoFileClip
import os

def get_youtube_transcript(url):

    # Handle normal youtube URL
    if "watch?v=" in url:
        video_id = url.split("watch?v=")[1].split("&")[0]

    # Handle short youtu.be URL
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]

    else:
        raise ValueError("Invalid YouTube URL")

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    full_text = " ".join([item.text for item in transcript])

    return full_text
def get_local_video_transcript(video_path):
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.mp3"
    video.audio.write_audiofile(audio_path)
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    os.remove(audio_path)
    return result["text"]

