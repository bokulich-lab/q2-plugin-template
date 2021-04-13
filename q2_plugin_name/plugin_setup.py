# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import (Plugin, Citations)

import q2_plugin_name

from q2_plugin_name import __version__

citations = Citations.load('citations.bib', package='q2_plugin_name')

plugin = Plugin(
    name='plugin-name',
    version=__version__,
    website="https://github.com/bokulich-lab/q2-plugin-name",
    package='q2_plugin_name',
    description=(
        'This is a template for building a new QIIME 2 plugin.'),
    short_description=(''),
)
