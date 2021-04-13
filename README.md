# q2-plugin-template
A skeleton for QIIME 2 plugins.

To use this template for a new plugin creation, you'll need to adjust the following elements:

- exchange `plugin_name` and `plugin-name` with the name of your plugin
- add versioneer support:
    - install versioneer [link](https://github.com/python-versioneer/python-versioneer): `pip install versioneer`
    - run `versioneer install`
    - add the `flake8: noqa` flag on top of the versioneer.py file 

Enjoy!
