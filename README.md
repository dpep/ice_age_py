ice_age
======
Freeze your ENVironment during testing. Just in case you need to change ENV variables during tests, this library ensures that everything is reset before the next test runs.

Current support limited to standard unittest framework.

### Install
```pip install ice_age```


### Usage
```python
from ice_age import TestCase

class MyTest(TestCase):
    def test_basic(self):
        ...

```

----
[![Build Status](https://travis-ci.org/dpep/ice_age_py.svg?branch=master)](https://travis-ci.org/dpep/ice_age_py)
[![Coverage Status](https://coveralls.io/repos/github/dpep/ice_age_py/badge.svg?branch=master)](https://coveralls.io/github/dpep/py_ice_age?branch=master)
[![installs](https://img.shields.io/pypi/dm/ice_age.svg?label=installs)](https://pypi.org/project/ice_age)
