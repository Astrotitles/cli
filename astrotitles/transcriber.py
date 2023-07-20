import warnings

warnings.filterwarnings("ignore")
import whisper_timestamped as whisper
from whisper_timestamped.make_subtitles import write_srt, write_vtt, split_long_segments
warnings.filterwarnings("default")

import utils
import os

class Transcriber:
    def __init__(self, args) -> None:
        self.input = utils.fileExists(args.pop("input"))
        self.output = utils.dirExists(args.pop("output"))
        self.format = args.pop("format")
        self.outputName = utils.outputFileName(args.pop("output_name"), self.format)
        self.maxChars = args.pop("max_chars")
        self.modelName = args.pop("model")

    def transcribe(self) -> None:
        model = whisper.load_model(self.modelName)

        warnings.filterwarnings("ignore")
        result = whisper.transcribe(model=model, audio=self.input, verbose=False)
        warnings.filterwarnings("default")

        outputFilePath = os.path.join(self.output, self.outputName)

        if os.path.exists(outputFilePath):
            utils.overrideOutputFilePrompt()

        with open(outputFilePath, "w", encoding="utf-8") as outputFile:
            if self.format == "srt":
                write_srt(self.getSubtitleData(result["segments"]), outputFile)
            else:
                write_vtt(self.getSubtitleData(result["segments"]), outputFile)
            
            outputFile.close()


    def getSubtitleData(self, segments):
        if self.maxChars == None:
            return segments
        else:
            return split_long_segments(segments, self.maxChars)

    @staticmethod
    def defaultModel() -> str:
        return "small"
    
    @staticmethod
    def availableModels() -> list[str]:
        return whisper.available_models()