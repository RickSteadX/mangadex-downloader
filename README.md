# mangadex-downloader

A command-line tool to download manga from [MangaDex](https://mangadex.org/), written in [Python](https://www.python.org/).

## Table of Contents

- [Key Features](#key-features)
- [Supported formats](#supported-formats)
- [Installation](#installation)
    - [From source](#installation-from-source)
    - [Docker](#installation-docker)
- [Usage](#usage)
    - [Python version](#usage-python-version)
    - [Docker version](#usage-docker-version)
- [Contributing](#contributing)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

## Key Features <a id="key-features"></a>

- Download manga, cover manga, chapter, or list directly from MangaDex
- Download manga or list from user library
- Find and download MangaDex URLs from MangaDex forums ([https://forums.mangadex.org/](https://forums.mangadex.org/))
- Download manga in each chapter, each volume, or wrap all chapters into a single file
- Search (with filters) and download manga
- Filter chapters by scanlation groups or users
- Manga tags, groups, and users blacklist support
- Batch download support
- Authentication (with cache) support
- Control how many chapters and pages you want to download
- Multi-language support
- Legacy MangaDex URL support
- Save as raw images, EPUB, PDF, Comic Book Archive (.cbz or .cb7)
- Respect API rate limit
- Option to skip oneshot chapters

## Supported formats <a id="supported-formats"></a>

See [docs/formats.md](docs/formats.md) for more info.

## Installation <a id="installation"></a>

Requirements:

- Python 3.10 or newer with pip

### From source <a id="installation-from-source"></a>

**NOTE:** You must have [git](https://git-scm.com/) installed.

```shell
git clone https://github.com/RickSteadX/mangadex-downloader.git
cd mangadex-downloader
pip install .
```

Or install directly from GitHub:

```shell
pip install git+https://github.com/RickSteadX/mangadex-downloader.git
```

The package is installed as `mangadex-downloader-rsx` (it provides the `mangadex-dl` and `mangadex-downloader` commands).

Optional dependencies:

- [py7zr](https://pypi.org/project/py7zr/) for cb7 support
- [orjson](https://pypi.org/project/orjson/) for a faster JSON library
- [lxml](https://pypi.org/project/lxml/) for EPUB support

To install all of them:

```shell
pip install ".[optional]"
```

### Docker <a id="installation-docker"></a>

Build the image from the repository:

```sh
git clone https://github.com/RickSteadX/mangadex-downloader.git
cd mangadex-downloader

# Base image
docker build -t mangadex-downloader .

# With optional dependencies (EPUB, cb7, etc.)
docker build -t mangadex-downloader:optional -f Dockerfile.optional .
```

## Usage <a id="usage"></a>

### Python version <a id="usage-python-version"></a>

```shell
mangadex-dl "insert MangaDex URL here"
# or
mangadex-downloader "insert MangaDex URL here"

# If the commands above don't work
python -m mangadex_downloader "insert MangaDex URL here"
```

### Docker version <a id="usage-docker-version"></a>

Downloaded files are stored in the `/downloads` directory inside the container.

```sh
docker run --rm -v /path/to/manga:/downloads mangadex-downloader "insert MangaDex URL"
```

More usage examples: [docs/cli_usage](docs/cli_usage/index.md)

All CLI options: [docs/cli_ref](docs/cli_ref/index.md)

## Contributing <a id="contributing"></a>

See [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

## Credits <a id="credits"></a>

Originally created by [Rahman Yusuf (@mansuf)](https://github.com/mansuf/mangadex-downloader).

## Disclaimer <a id="disclaimer"></a>

mangadex-downloader is not affiliated with MangaDex.
