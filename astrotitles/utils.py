import argparse
import pathlib
import os
from time import time

def checkPositive(value) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue


def fileExists(path: str) -> str:
    if pathlib.Path(path).is_file():
        return path
    else:
        raise argparse.ArgumentError(None, "File does not exist")


def dirExists(path: str) -> str:
    if pathlib.Path(path).is_dir():
        return path
    else:
        raise argparse.ArgumentError(None, "Directory does not exist")


def generateName() -> str:
    return f"subtitle_{str(time()).replace('.', '')}"


def outputFileName(outputName: str, format: str) -> str:
    return f"{generateName() if outputName == None else outputName}.{format}"


def verbose(msg: str, verbose: bool) -> None:
    if (verbose):
        print(msg)


def overrideOutputFilePrompt(outputFilePath: str) -> None:
    override = input("\nOutput file already exists. Override [y/n]: ")

    if override != "y":
        print("Aborting file save...")
        exit()
    else:
        os.remove(outputFilePath)