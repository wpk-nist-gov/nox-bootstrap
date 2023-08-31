# Installation

## Stable release

To install nox-bootstrap, run this command in your terminal:

```bash
pip install nox-bootstrap
```

or

```bash
conda install -c wpk-nist nox-bootstrap
```

This is the preferred method to install nox-bootstrap, as it will always install
the most recent stable release.

## From sources

The sources for nox-bootstrap can be downloaded from the [Github repo].

You can either clone the public repository:

```bash
git clone git://github.com/wpk-nist-gov/nox-bootstrap.git
```

Once you have a copy of the source, you can install it with:

```bash
pip install .
```

To install dependencies with conda/mamba, use:

```bash
conda env create [-n {name}] -f environment/base.yaml
conda activate {name}
pip install [-e] --no-deps .
```

If `environment/base.yaml` does not exist, it can be generated with:

```bash
pip/pipx install pyproject2conda
pyproject2conda yaml -o environment/base.yaml
```

where options in brackets are options (for environment name, and editable
install, respectively).

[github repo]: https://github.com/wpk-nist-gov/nox-bootstrap
