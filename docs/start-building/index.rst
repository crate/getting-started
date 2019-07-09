.. _start-building:

==============
Start building
==============

CrateDB is happy at the heart of any application stack, with a number of
libraries to support development.

Below is a selection of development libraries that are known to work with
CrateDB. This is split into two categories: software that is maintained by
Crate.io, and software that is maintained by the CrateDB community.

Pick your library, and start building!

+-----------+-------------+-------------------------------+------------------+
| Language  | Maintainers | Drivers                       | Plugins and ORMs |
+===========+=============+===============================+==================+
| Java      | Crate.io    | `crate-jdbc`_                 |                  |
+-----------+-------------+-------------------------------+------------------+
| Python    | Crate.io    | `crate`_                      | `SQLAlchemy`_    |
+-----------+-------------+-------------------------------+------------------+
| PHP       | Crate.io    | `CrateDB PDO`_                | `DBAL`_          |
+-----------+-------------+-------------------------------+------------------+
| C# (.NET) | Crate.io    | `Npgsql`_                     |                  |
+-----------+-------------+-------------------------------+------------------+
| Python    | Community   | `asyncpg`_                    |                  |
+-----------+-------------+-------------------------------+------------------+
| Ruby      | Community   | `crate_ruby`_                 | `ActiveRecord`_  |
+-----------+-------------+-------------------------------+------------------+
| Scala     | Community   | `crate-scala`_                |                  |
+-----------+-------------+-------------------------------+------------------+
| Node.js   | Community   | `crate-connect`_, `cratejs`_, | `Loopback`_      |
|           |             | `node-crate`_                 |                  |
+-----------+-------------+-------------------------------+------------------+
| Go        | Community   | `pgx`_                        |                  |
+-----------+-------------+-------------------------------+------------------+
| Perl      | Community   | `DBD::Crate`_                 |                  |
+-----------+-------------+-------------------------------+------------------+
| Erlang    | None (EOL)  | `craterl`_                    |                  |
+-----------+-------------+-------------------------------+------------------+

If you would like to see something added to this page, please `get in touch`_.

.. _ActiveRecord: https://rubygems.org/gems/activerecord-crate-adapter
.. _asyncpg: https://github.com/MagicStack/asyncpg
.. _crate_ruby: https://rubygems.org/gems/crate_ruby
.. _crate-connect: https://www.npmjs.com/package/crate-connect
.. _crate-jdbc: https://crate.io/docs/clients/jdbc/en/latest/
.. _crate-scala: https://github.com/alexanderjarvis/crate-scala
.. _crate: https://crate.io/docs/clients/python/en/latest/
.. _Crate.Client: https://github.com/mfussenegger/crate-mono
.. _CrateDB PDO: https://crate.io/docs/clients/pdo/en/latest/
.. _cratejs: https://www.npmjs.com/package/cratejs
.. _craterl: https://github.com/crate/craterl
.. _DBAL: https://crate.io/docs/clients/dbal/en/latest/
.. _DBD::Crate: https://github.com/mamod/DBD-Crate
.. _get in touch: https://crate.io/contact/
.. _Loopback: https://github.com/lovelysystems/loopback-connector-crateio
.. _node-crate: https://www.npmjs.com/package/node-crate
.. _Npgsql: https://crate.io/docs/clients/npgsql/en/latest/
.. _pgx: https://github.com/jackc/pgx
.. _SQLAlchemy: https://crate.io/docs/clients/python/en/latest/sqlalchemy.html
