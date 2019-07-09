===============
Developer Guide
===============

Prerequisites
=============

Python 3.7 is required.

Documentation
=============

The docs are written with ReStructuredText_ and processed with Sphinx_.

Change into the ``docs`` directory:

.. code-block:: console

    $ cd docs

To see a list of options, run:

    $ make help

If you want live rebuilding of the docs, you must install `fswatch`_.

The live docs are automatically built from Git by `Read the Docs`_.

.. _Read the Docs: http://readthedocs.org
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/
.. _fswatch: https://github.com/emcrisostomo/fswatch
