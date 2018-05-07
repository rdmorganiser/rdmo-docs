Testing
=======

Setup tests
-----------

First, create a ``local.py`` file:

.. code:: bash

    cp testing/config/settings/sample.local.py testing/config/settings/local.py

Afterwards edit the ``local.py`` as for a regular RDMO instance.

Running tests
-------------

.. code:: bash

    python testing/runtests.py
    python testing/runtests.py -k              # keep the database between test runs
    python testing/runtests.py rdmo.domain     # test only the domain app


Coverage
--------

.. code:: bash

    coverage run testing/runtests.py
    coverage report                     # show a coverage report in the terminal
    coverage html                       # create browsable coverage report in htmlcov/
