===============
Developer Guide
===============

Prerequisites
=============

Python 3.7 is required.

If you want live rebuilding of the docs, you must install `fswatch`_.

Documentation
=============

|style|

The docs are written with ReStructuredText_ and processed with Sphinx_.

Developing
----------

Change into the ``docs`` directory:

.. code-block:: console

    $ cd docs

To see a list of options, run:

.. code-block:: console

    $ make help

    Crate Documentation Build System

    Run `make <TARGET>`, where <TARGET> is one of:

      dev     Run a Sphinx development server that builds and lints the
              documentation as you edit the source files

      check   Build, test, and lint the documentation (run by CI)

      clean   Clean up (e.g., remove lint files)

      reset   Reset the source

Tests
-----

|travis|

Deployment
----------

|rtd|

The live docs are automatically built from Git by `Read the Docs`_.


.. _Read the Docs: http://readthedocs.org
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/
.. _fswatch: https://github.com/emcrisostomo/fswatch


.. |style| image:: https://img.shields.io/endpoint.svg?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcrate%2Fgetting-started%2Fmaster%2Fdocs%2Fstyle.json
    :alt: Style version
    :target: https://github.com/crate/crate-docs-style

.. |travis| image:: https://img.shields.io/travis/crate/getting-started.svg?style=flat
    :alt: Travis CI status
    :scale: 100%
    :target: https://travis-ci.org/crate/getting-started

.. |rtd| image:: https://readthedocs.org/projects/crate-getting-started/badge/?version=latest
    :alt: Read The Docs status
    :scale: 100%
    :target: https://crate-getting-started.readthedocs.io/en/latest/?badge=latest

