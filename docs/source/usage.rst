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

Executing tasks (API token required)
----------------
The tasks can be performed by using the script ``bhtom2_scripts.py`` or by importing as a module class named :py:class:`BHTasks`.
Before that however, the user must have a token for using BHTOM2 API. To get a token, see the `BHTOM2 API documentation <https://github.com/BHTOM-Team/bhtom2/blob/bhtom2-dev/Documentation/DocumentationAPI.md>`_.
After getting the token, using the script or the module requires the user to pass the token to the script. This can be done in two ways:
 - Passing the token with an argument ``--token`` when running the script.
 - Creating a file named ``.env`` in the root directory of the project with the following content:
   **BHTOM2_API_TOKEN=your_api_token**

When user wants to import the module, the token must be passed as an argument to the class constructor.
::
   from bhtom2_scripts import BHTasks
   tasks = BHTasks('YOUR_API_TOKEN')


Using the script
----------------
Running the script ``bhtom2_scripts.py`` with the desired task as argument.
Possible tasks are:
 - ``obs``: Get the list of observatories from the BHTOM2 database. Save the list to a CSV file.
 - ``cam``: Get the list of cameras from the BHTOM2 database. Save the list to a CSV file.
 - ``map``: Generate a map with the observatories from the BHTOM2 database (NOT WORKING YET!)

Commands below are assuming you have ``.env`` file, otherwise pass ``--token YOUR_API_TOKEN`` argument to the script.

To get the list of observatories:
::
   python3 bhtom2-scripts.py obs

To get the list of cameras:
::
   python3 bhtom2-scripts.py cam

To get specification of a chosen camera, run:
::
   python3 bhtom2-scripts.py cam --prefix CAMERA_PREFIX

Importing as a module
---------------------
The module :py:mod:`bhtom2_scripts.py` contains a class named :py:class:`BHTasks` that can be used to perform the same tasks as the script.

To get the list of observatories, run:
::
   from bhtom2_scripts import BHTasks
   tasks = BHTasks('YOUR_API_TOKEN')
   tasks.do_obs()

This will return a pandas DataFrame with the list of observatories.

To get the list of cameras, run:
::
   from bhtom2_scripts import BHTasks
   tasks = BHTasks('YOUR_API_TOKEN')
   tasks.do_cam()

This will return a pandas DataFrame with the list of cameras.

To get specification of a chosen camera, run:
::
   from bhtom2_scripts import BHTasks
   tasks = BHTasks('YOUR_API_TOKEN')
   tasks.do_cam('CAMERA_PREFIX')