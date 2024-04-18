Usage
=====

.. _installation:

Installation
------------
 The module requires Python 3.6 or higher and the following packages:
   - requests
   - python-dotenv
   - pandas

.. To use bhtom2-scripts, first install it using pip:

.. .. code-block:: console

..    (.venv) $ pip install bhtom2_scripts

Executing tasks
----------------
The tasks can be performed by using the script ``bhtom2_scripts.py`` or by importing as a module class named :py:class:`BHTasks`.

Using the script
----------------
Running the script ``bhtom2_scripts.py`` with the desired task as argument.
Possible tasks are:
 - ``obs``: Get the list of observatories from the BHTOM2 database.
 - ``cam``: Get the list of cameras from the BHTOM2 database.
 - ``map``: Generate a map with the observatories from the BHTOM2 database (NOT WORKING YET!)

To get the list of observatories, run:
::
   python3 bhtom2-scripts.py obs

To get the list of cameras, run:
::
   python3 bhtom2-scripts.py cam

Importing as a module
---------------------
The module :py:mod:`bhtom2_scripts.py` contains a class named :py:class:`BHTasks` that can be used to perform the same tasks as the script.

To get the list of observatories, run:
::
   from bhtom2_scripts import BHTasks
   tasks = BHTasks()
   tasks.do_obs()

This will return a pandas DataFrame with the list of observatories.

To get the list of cameras, run:
::
   from bhtom2_scripts import BHTasks
   tasks = BHTasks()
   tasks.do_cam()

This will return a pandas DataFrame with the list of cameras.