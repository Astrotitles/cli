import argparse

from astrotitles.utils import checkPositive
from astrotitles.transcriber import Transcriber

from whisper.utils import str2bool

def cli():
    parser = argparse.ArgumentParser(
        prog="astrotitles",
        description="Generate a srt/vtt subtitle file from audio/video file",
        epilog="Thanks for using Astrotitles CLI!"
    )

    parser.add_argument("input", type=str, help="Input audio/video file to be transcribed")

    parser.add_argument("--output", type=str, default="./", help="Specify output directory for srt/vtt subtitle file")
    parser.add_argument("--output-name", type=str, help="Specify output file name (no extension)")
    parser.add_argument("--max-chars", type=checkPositive, help="Specify the maximum number of characters allowed per subtitle segment")
    parser.add_argument("--format", type=str, default="srt", choices=["srt", "vtt"], metavar="FORMAT", help="Specify subtitle format (default: .srt)")
    parser.add_argument("--model", type=str, default=Transcriber.defaultModel(), choices=Transcriber.availableModels(), metavar="MODEL", help="Whisper AI model to use for transcribing")
    parser.add_argument("--verbose", type=str2bool, default=True, help="Print out progress of transcription process (default: True)")

    args = parser.parse_args().__dict__

    transcriber = Transcriber(args)
    transcriber.transcribe()

if __name__ == "__main__":
    cli()