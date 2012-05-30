python-filetype
========

Mike Jensen <jjensen.mike at gmail.com>

Distributed under the PSF License: http://www.python.org/psf/license/

An extension on the functionality provided by python-magic (https://github.com/ahupp/python-magic)

Originally wrote for VAVE xml feed destructor (https://github.com/votinginfoproject/VAVE)

Installation
========

All of these require a currently installed version of python-magic and all of its dependencies

Run:

python setup.py install

Examples
========

import filetype

filetype.get_type("testdata/test.csv")

'csv'

filetype.get_type("testdata/test.gz")

'gz'

filetype.is_compression("testdata/test.tar")

False

filetype.is_compression("testdata/test.bz2")

True

filetype.is_compression_by_type("zip")

False

filetype.is_archived("testdata/test.zip")

True
