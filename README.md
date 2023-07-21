<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />

<h3 align="center">Astrotitles CLI</h3>

  <p align="center">
    Automatically generate subtitles using the Astrotitles command line interface.
    <br />
    <br />
    <a href="https://astrotitles.com">View Web App</a>
    ·
    <a href="https://github.com/Astrotitles/cli/issues">Report Bug</a>
    ·
    <a href="https://github.com/Astrotitles/cli/issues">Request Feature</a>
  </p>
</div>

## Getting Started

Astrotitles CLI is a tool that allows you to generate a srt/vtt subtitle file from a audio/video file. Astrotitles has word-level timestamps, allowing you to control how many characters are in each subtitle segment.

### Prerequisites

- Python: https://www.python.org/downloads/

### Installation

1. Install via pip
   ```sh
   pip install astrotitles
   ```
2. Install via pip (github)
   ```sh
   pip install git+https://github.com/Astrotitles/cli.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The Astrotitles CLI is self-documented with ```--help``` content and examples for every command. You should start exploring the CLI by using the global ```--help``` option:

```sh
astrotitles --help
```

```
usage: astrotitles [-h] [--output OUTPUT] [--output-name OUTPUT_NAME] [--max-chars MAX_CHARS] 
    [--format FORMAT] [--model MODEL] [--verbose VERBOSE] input

Generate a srt/vtt subtitle file from audio/video file

positional arguments:
  input                 Input audio/video file to be transcribed

options:
  -h, --help            show this help message and exit
  --output OUTPUT       Specify output directory for srt/vtt subtitle file
  --output-name OUTPUT_NAME
                        Specify output file name (no extension)
  --max-chars MAX_CHARS
                        Specify the maximum number of characters allowed per subtitle segment
  --format FORMAT       Specify subtitle format (default: .srt)
  --model MODEL         Whisper AI model to use for transcribing
  --verbose VERBOSE     Print out progress of transcription process (default: True)

Thanks for using Astrotitles CLI!
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## License

Distributed under the AGPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact

- [Ben Webster](https://benwebs.com)
- Project: [https://github.com/Astrotitles/cli](https://github.com/Astrotitles/cli)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


Thanks for using Astrotitles! 🔥

[contributors-shield]: https://img.shields.io/github/contributors/Astrotitles/cli.svg?style=for-the-badge
[contributors-url]: https://github.com/Astrotitles/cli/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Astrotitles/cli.svg?style=for-the-badge
[forks-url]: https://github.com/Astrotitles/cli/network/members
[stars-shield]: https://img.shields.io/github/stars/Astrotitles/cli.svg?style=for-the-badge
[stars-url]: https://github.com/Astrotitles/cli/stargazers
[issues-shield]: https://img.shields.io/github/issues/Astrotitles/cli.svg?style=for-the-badge
[issues-url]: https://github.com/Astrotitles/cli/issues
[license-shield]: https://img.shields.io/github/license/Astrotitles/cli.svg?style=for-the-badge
[license-url]: https://github.com/Astrotitles/cli/blob/master/LICENSE.txt