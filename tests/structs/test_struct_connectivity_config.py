##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2022 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import unittest

import pykerio
from pykerio.enums import ConnectivityType


class TestCase_ConnectivityConfig(unittest.TestCase):
    def test_01_ConnectivityConfig(self):
        """
        Test ConnectivityConfig
        """
        mode = ConnectivityType.Persistent
        probehosts = pykerio.structs.OptionalString({'enabled': True,
                                                     'value': '192.168.1.1'})

        teststruct = pykerio.structs.ConnectivityConfig({
            'mode': mode,
            'probeHosts': probehosts,
            'reconnectTunnelsWhenPrimaryGoesBack': True,
            'lazyFailover': False})
        self.assertEqual(len(teststruct.keys()), 4)
        self.assertEqual(len(teststruct.values()), 4)

        self.assertEqual(teststruct['mode'], mode)
        self.assertEqual(teststruct['probeHosts'], probehosts)
        self.assertEqual(teststruct['reconnectTunnelsWhenPrimaryGoesBack'],
                         True)
        self.assertEqual(teststruct['lazyFailover'], False)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
