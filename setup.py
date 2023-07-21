from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    version="0.1.5",
    name="astrotitles",
    packages=find_packages(),
    license="AGPL-3.0",
    author="Ben Webster",
    url="https://github.com/Astrotitles/cli",
    download_url="https://github.com/Astrotitles/cli.git",
    keywords=["AI", "Whisper AI", "Subtitles"],
    install_requires=[
        'whisper_timestamped',
    ],
    description="Automatically generate subtitles using the Astrotitles command line interface.",
    long_description=long_description,
    long_description_content_type="markdown",
    entry_points={
        'console_scripts': ['astrotitles=astrotitles.cli:cli'],
    },
    include_package_data=True,
)