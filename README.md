# pycsvdemo

Python CSV handling demo

## Installation

Clone this repository, then make it the working directory:

```console
git clone https://github.com/bowmanjd/pycsvdemo.git
cd pycsvdemo
```

> Recommended: [create a virtual environment and activate it](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko). Then, `pip install -e .`

## Usage

```console
python csvdemo.py -e utf-8-sig samples/sample-utf8bom.csv out/sample-transformed.csv
```

> If you installed in a currently active virtual environment, as recommended above, you can use a shorter form: `csvdemo -e utf-8-sig samples/sample-utf8bom.csv out/sample-transformed.csv`

## Contributing

Please feel free to submit pull requests and/or open issues.

## License

Copyright 2020 Jonathan Bowman. All documentation and code contained in this repository may be freely shared in compliance with [the Apache License, Version 2.0][apache 2.0], and is provided “AS IS” without warranties or conditions of any kind.

[apache 2.0]: http://www.apache.org/licenses/LICENSE-2.0
