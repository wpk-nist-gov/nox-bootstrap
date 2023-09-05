<!-- markdownlint-disable MD041 -->

[![Repo][repo-badge]][repo-link] <!-- [![Docs][docs-badge]][docs-link] -->
[![PyPI license][license-badge]][license-link]

<!-- [![PyPI version][pypi-badge]][pypi-link] -->
<!-- [![Conda (channel only)][conda-badge]][conda-link] -->

[![Code style: black][black-badge]][black-link]

<!--
  For more badges, see
  https://shields.io/category/other
  https://naereen.github.io/badges/
  [pypi-badge]: https://badge.fury.io/py/nox-bootstrap
-->

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/psf/black

<!-- [pypi-badge]: https://img.shields.io/pypi/v/nox-bootstrap -->
<!-- [pypi-link]: https://pypi.org/project/nox-bootstrap -->
<!-- [docs-badge]: https://img.shields.io/badge/docs-sphinx-informational -->
<!-- [docs-link]: https://pages.nist.gov/nox-bootstrap/ -->

[repo-badge]: https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff
[repo-link]: https://github.com/wpk-nist-gov/nox-bootstrap

<!-- [conda-badge]: https://img.shields.io/conda/v/wpk-nist/nox-bootstrap -->
<!-- [conda-link]: https://anaconda.org/wpk-nist/nox-bootstrap -->

[license-badge]: https://img.shields.io/pypi/l/cmomy?color=informational
[license-link]: https://github.com/wpk-nist-gov/nox-bootstrap/blob/main/LICENSE

<!-- other links -->

[nox]: https://github.com/wntrblm/nox
[pipx]: https://github.com/pypa/pipx

# `nox-bootstrap`

A meta package to bootstrap [nox] controlled environment.

## Overview

I use nox to manage development environments as well as testing/linting/typing
environments. This meta package makes it easy to bootstrap the creation of a
development environment with [pipx]:

```bash
pipx run --spec git+https://github.com/wpk-nist-gov/nox-bootstrap.git \
     nox -s bootstrap -- \
     --python-paths "~/.conda/envs/test-3.*/bin" \
     --dev-extras dev nox
```

Where to commands and options passed to [nox] are project specific. See
[here](https://pages.nist.gov/thermoextrap/contributing.html) for example usage.
If the above command creates a development environment with nox requirements,
then you can bootstrap your working environment with one command.

## Status

This package is actively used by the author. Please feel free to create a pull
request for wanted features and suggestions!

<!-- end-docs -->

## License

This is free software. See [LICENSE][license-link].

## Related work

This is used in the following projects:

- [cmomy]
- [tmmc-lnpy]
- [thermoextrap]
- [analphipy]
- [module-utilities]
- [pyproject2conda]

[cmomy]: https://github.com/usnistgov/cmomy
[tmmc-lnpy]: https://github.com/usnistgov/tmmc-lnpy
[thermoextrap]: https://github.com/usnistgov/thermoextrap
[analphipy]: https://github.com/usnistgov/analphipy
[module-utilities]: https://github.com/usnistgov/module-utilities
[pyproject2conda]: https://github.com/wpk-nist-gov/pyproject2conda

## Contact

The author can be reached at <wpk@nist.gov>.

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[wpk-nist-gov/cookiecutter-pypackage](https://github.com/wpk-nist-gov/cookiecutter-pypackage)
Project template forked from
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
