# PDF Read

<div align="left">


![Action Status](https://github.com/psf/black/workflows/Test/badge.svg)
![Action Status](https://camo.githubusercontent.com/2c8b15a3902bc15c0d1e6d70bbf7a1f0f248e2df4b430e25517c7543233530fb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f7665726167652d3130302532352d627269676874677265656e2e737667)
![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

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
