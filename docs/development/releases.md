Releases
========

0) Install `rdmo[dev]`.

1) Ensure tests are passing.

3) Check that version in `rdmo/__init__.py`, `CHANGELOG.md` and *all the other things* are up to date.

4) Build production front-end files, source-distribution and wheel using:

  ```python
  rdmo-admin build
  ```

  which calls `npm ci` and `npm run build:prod` and `python -m build`

5) Upload with `twine` to Test PyPI:

  ```
  twine upload -r testpypi dist/*
  ```

6) Check https://test.pypi.org/project/rdmo/.

7) Upload with `twine` to PyPI:

  ```
  twine upload dist/*
  ```

8) Check https://pypi.org/project/rdmo/.

9) Create release on [GitHub](https://github.com/rdmorganiser/rdmo/releases).
