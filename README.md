# q2-plugin-template
A skeleton for QIIME 2 plugins.

To use this template for a new plugin creation, you'll first need to create a new plugin repo by clicking the `Use this template` button.
Fill out the new repository name and description. Following that initial setup, in your new plugin repo you still
need to adjust the following elements:

- exchange `plugin_name` and `plugin-name` with the name of your plugin
- adjust all the required fields in `setup.py` and `plugin_setup.py`
- add `versioneer` support for version management:
    - install `versioneer` [(link)](https://github.com/python-versioneer/python-versioneer) into any python environment: `pip install versioneer`
    - from the project directory, run `versioneer install` to create/modify all the required files
    - add the `# flake8: noqa` flag on top of the `versioneer.py` file for the file to be ignore by lint checks

Enjoy!
