.. _mac-install:

==================================
Install CrateDB on Mac OS |nbsp| X
==================================

.. prevent widowed "x" in sidebar nav

.. |nbsp| unicode:: 0xA0
   :trim:

Because CrateDB is a Java application, it runs effortlessly on macOS.

.. SEEALSO::

   These instructions are designed to get you up and running on your personal
   computer.

   For putting CrateDB into production, you can learn more about
   `deploying`_ or `scaling`_ CrateDB in the `CrateDB Guide`_.

.. rubric:: Table of contents

.. contents::
   :local:

One-step setup
==============

You can install and run CrateDB on macOS with one simple command in your
terminal application:

.. code-block:: console

   sh$ bash -c "$(curl -L https://try.crate.io/)"

If you don't already have `Java 11`_ installed, the above command will try to
take care of that for you along with a few other housekeeping tasks.

.. NOTE::

   CrateDB performs a number of `bootstrap checks`_ on startup.

Next steps
==========

Now you have CrateDB up and running, it's time to :ref:`import some test data
<import-test-data>`.

.. _bootstrap checks: https://crate.io/docs/crate/guide/en/latest/admin/bootstrap-checks.html
.. _Java 11: https://www.oracle.com/technetwork/java/javase/downloads/index.html
.. _Oracle's Java: http://www.java.com/en/download/help/mac_install.xml
.. _CrateDB Guide: https://crate.io/docs/crate/guide/en/latest/
.. _deploying: https://crate.io/docs/crate/guide/en/latest/deployment/index.html
.. _scaling: https://crate.io/docs/crate/guide/en/latest/scaling/index.html
