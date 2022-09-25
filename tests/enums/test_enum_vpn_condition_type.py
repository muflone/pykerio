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

from pykerio.enums import VpnConditionType


class TestCase_VpnConditionType(unittest.TestCase):
    def test_00_IncomingClient(self):
        """
        Test VpnConditionType with IncomingClient
        """
        value = VpnConditionType.IncomingClient
        self.assertEqual(value.dump(), 'IncomingClient')
        self.assertEqual(value.name, 'IncomingClient')
        self.assertEqual(value.value, 0)

    def test_01_SelectedTunnel(self):
        """
        Test VpnConditionType with SelectedTunnel
        """
        value = VpnConditionType.SelectedTunnel
        self.assertEqual(value.dump(), 'SelectedTunnel')
        self.assertEqual(value.name, 'SelectedTunnel')
        self.assertEqual(value.value, 1)

    def test_02_AllTunnels(self):
        """
        Test VpnConditionType with AllTunnels
        """
        value = VpnConditionType.AllTunnels
        self.assertEqual(value.dump(), 'AllTunnels')
        self.assertEqual(value.name, 'AllTunnels')
        self.assertEqual(value.value, 2)
