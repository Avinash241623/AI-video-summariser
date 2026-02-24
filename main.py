from transcript import get_youtube_transcript, get_local_video_transcript
from summarizer import summarize_text
from translator import translate_text
def main():
        choice = input("Enter 1 for YouTube link, 2 for Local video: ")
        if choice == "1":
            url = input("Enter YouTube URL: ")
            transcript = get_youtube_transcript(url)
        elif choice == "2":
            path = input("Enter video file path: ")
            transcript = get_local_video_transcript(path)
        else:
            print("Invalid choice")
            return
        summary = summarize_text(transcript)
        print("\n--- English Summary ---\n")
        print(summary)
        languages = ["hi", "es", "fr", "de", "te"]
        for lang in languages:
            translated = translate_text(summary, lang)
            print(f"\n--- Summary in {lang} ---\n")
            print(translated)
if __name__ == "__main__":
    main()