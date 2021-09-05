# PDF Read

<div align="left">


[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml)

</div>


## Requirements
* [Python 3.7+](https://python.org)
* [Python-Pooetry 1.1.8+](https://python-poetry.org/)

## 🤯 How to use it


1. Clone the repo:

```bash
git clone https://github.com/wilsonmoraes/pdf-read
```
2. Install dependencies:

```bash
poetry install
```


3. create .env configuration:

```bash
cp local.env .env
```

4.  inform `.env` values according to:

|             Propertie             |           Value            |
| :------------------------------ | :--------------------------- |
|   `PDFS_FOLDER`   | folder containing all pdf files |
|    `EXPORT_CSV_TO_FOLDER`    |  folder name to create csv  |

5. run the follow command and wait 😎


```bash
make run
```
