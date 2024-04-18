Usage
=====

.. _installation:

.. Installation
.. ------------

.. To use bhtom2-scripts, first install it using pip:

.. .. code-block:: console

..    (.venv) $ pip install bhtom2-scripts

Executing tasks
----------------
The tasks can be performed by using the script ``bhtom2-scripts.py`` or by importing as a module class named :py:class:`BHTasks`.

.. _bhtom2-scripts.py:

.. Using the script
.. ----------------
Tasks can be executed by running the script ``bhtom2-scripts.py`` with the desired task as argument.
Possible tasks are:
 - ``obs``: Get the list of observatories from the BHTOM2 database.
 - ``cam``: Get the list of cameras from the BHTOM2 database.
 - ``map``: Generate a map with the observatories from the BHTOM2 database (NOT WORKING YET!)

To get the list of observatories, run:
::

   $ bhtom2-scripts.py obs

To get the list of cameras, run:
::

   $ bhtom2-scripts.py cam
