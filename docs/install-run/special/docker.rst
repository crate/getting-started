.. _docker-install:

=====================
Run CrateDB on Docker
=====================

CrateDB and Docker_ are a great match thanks to CrateDB's shared-nothing,
horizontally scalable architecture that lends itself well to containerization.

.. rubric:: Table of contents

.. contents::
   :local:

One-step setup
==============

Spin up the official CrateDB Docker image, like so:

.. code-block:: console

   sh$ docker run -p "4200:4200" crate

.. TIP::

   If this command aborts with an error, consult the `troubleshooting guide`_.

.. CAUTION::

   This command will get you up and running for the first time.

   By default, the CrateDB Docker image stores data inside the container. If
   you delete the container, the data will be deleted along with it. When
   you're ready to start using CrateDB for data that you care about, you should
   consult the `full guide to CrateDB and Docker`_.

Next steps
==========

Now you have CrateDB up and running, it's time to :ref:`import some test data
<import-test-data>`.

.. _troubleshooting guide: https://crate.io/docs/crate/guide/en/latest/deployment/containers/docker.html#docker-troubleshooting
.. _bootstrap check: https://crate.io/docs/crate/guide/en/latest/admin/bootstrap-checks.html
.. _CrateDB Docker image: https://hub.docker.com/_/crate/
.. _Docker: https://www.docker.com/
.. _full guide to CrateDB and Docker: https://crate.io/docs/crate/guide/en/latest/deployment/containers/docker.html
.. _resource constraints: https://crate.io/docs/crate/guide/en/latest/deployment/containers/docker.html#resource-constraints
