.. _linux-install:

========================
Install CrateDB on Linux
========================

CrateDB maintains packages for `Debian GNU/Linux`_, `Ubuntu`_, and `RedHat
Linux`_.

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

You can download and run CrateDB on one of these operating systems with one
simple command in your terminal application:

.. code-block:: console

   sh$ bash -c "$(curl -L https://try.crate.io/)"

Next steps
==========

Now you have CrateDB up and running, it's time to :ref:`import some test data
<import-test-data>`.

.. _bootstrap checks: https://crate.io/docs/crate/guide/en/latest/admin/bootstrap-checks.html
.. _OpenJDK: http://openjdk.java.net/projects/jdk8/
.. _CrateDB Guide: https://crate.io/docs/crate/guide/en/latest/
.. _deploying: https://crate.io/docs/crate/guide/en/latest/deployment/index.html
.. _scaling: https://crate.io/docs/crate/guide/en/latest/scaling/index.html
.. _Debian GNU/Linux: https://crate.io/docs/crate/guide/en/latest/deployment/linux/debian.html
.. _Ubuntu: https://crate.io/docs/crate/guide/en/latest/deployment/linux/ubuntu.html
.. _RedHat Linux: https://crate.io/docs/crate/guide/en/latest/deployment/linux/red-hat.html
