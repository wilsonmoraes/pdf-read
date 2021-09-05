# PDF Read

<div align="left">


[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml)

</div>


## Requirements
* [Python 3.7+](https://python.org)
* [Python-Pooetry 1.1.8+](https://python-poetry.org/)

### Development features

- Supports `Python 3.7` and higher.
- [`Poetry`](https://python-poetry.org/) as a dependencies manager.
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) .
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).

## 🤯 How to use it


1. Clone the repo:

```bash
git clone https://github.com/wilsonmoraes/pdf-read
```

2. Create .env configuration:

```bash
cp local.env .env
```

3.  Set `.env` values like:

|             Propertie             |           Value            |
| :------------------------------ | :--------------------------- |
|   `INPUT_DIR`   | Folder containing pdfs files |
|    `OUT_DIR`    |  CSV data exported to directory. Files will be: `OUT_DIR/dd_mm_yyyy_hh_mm_ss.csv` |

4. Run the follow command and wait 😎


```bash
make run
```
