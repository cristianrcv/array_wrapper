<!-- Codacy -->
[![Codacy grade](https://api.codacy.com/project/badge/Grade/d5bf54f5febd40c380d0514244a19b4a)](https://www.codacy.com/app/cristianrcv/array_wrapper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cristianrcv/array_wrapper&amp;utm_campaign=Badge_Grade)

<!-- Main Repository language -->
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1a16d97b1ea2466bba4950b7749b16a9)](https://app.codacy.com/app/cristianrcv/array_wrapper?utm_source=github.com&utm_medium=referral&utm_content=cristianrcv/array_wrapper&utm_campaign=badger)
[![Language](https://img.shields.io/badge/language-python-brightgreen.svg)](https://img.shields.io/badge/language-python-brightgreen.svg)

<!-- Repository License -->
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/cristianrcv/pycompss-pluto/blob/master/LICENSE)


# Array Wrapper

A C Extension for Python to wrap arrays so that they are continuous in memory and
can be accessed by memory address. 


---

## Table of Contents

* [Dependencies](#dependencies)
    * [Software Dependencies](#software-dependencies)
    * [Python Module Dependencies](#python-module-dependencies)
    * [Extra Dependencies](#extra-dependencies)
* [Commands](#commands)
    * [Build](#build)
    * [Test](#test)
    * [Style](#style)
    * [Clean](#clean)
* [Contributing](#contributing)
* [Author](#author)
* [Disclaimer](#disclaimer)
* [License](#license)

---


## Dependencies

### Software Dependencies

[Cython][cython]: Cython is an optimising static compiler for both the Python
programming language and the extended Cython programming language (based on 
Pyrex). It makes writing C extensions for Python as easy as Python itself.


### Python Module Dependencies

- [Cython][cython] Python module
- [UnitTest][unittest] Python module


### Extra Dependencies

- To run all tests you require the [Nose][nose] Python module


## Commands

### Build

For an in-situ build run:

```
./install.sh
```

### Test

With debug mode enabled:

```
export PYTHONPATH=${git_base_dir}
python nose_tests.py -s
```

With debug mode disabled:

```
export PYTHONPATH=${git_base_dir}
python -O nose_tests.py
```


### Style

This project follows the [PyCodeStyle guide][pycodestyle] (formerly called pep8).

This project tolerates the following relaxations:
* `E501 line too long` : Code lines can be up to 120 characters

You can verify the code style by running:

```
pycodestyle . --max-line-length=120
```


### Clean

```
./clean.sh
```

## Contributing

All kinds of contributions are welcome. Please do not hesitate to open a new issue,
submit a pull request or contact the author if necessary. 
 

## Author

Cristián Ramón-Cortés Vilarrodona <cristian.ramoncortes(at)bsc.es> ([Personal WebPage][cristian])

This work is supervised by:
- Rosa M. Badia ([BSC][bsc])
- Philippe Clauss ([INRIA][inria])
- Jorge Ejarque ([BSC][bsc])


## Disclaimer

This is part of a collaboration between the [CAMUS Team][camus] at [INRIA][inria] and
the [Workflows and Distributed Computing Team][wdc-bsc] at [BSC][bsc] and is still
under development. 


## License

Licensed under the [Apache 2.0 License][apache-2]


[cython]: http://cython.org/

[unittest]: https://docs.python.org/2/library/unittest.html

[nose]: https://nose.readthedocs.io/en/latest/
[pycodestyle]: https://pypi.python.org/pypi/pycodestyle

[camus]: https://www.inria.fr/en/teams/camus
[inria]: https://www.inria.fr/
[wdc-bsc]: https://www.bsc.es/discover-bsc/organisation/scientific-structure/workflows-and-distributed-computing
[bsc]: https://www.bsc.es/
[cristian]: https://cristianrcv.netlify.com/

[apache-2]: http://www.apache.org/licenses/LICENSE-2.0
