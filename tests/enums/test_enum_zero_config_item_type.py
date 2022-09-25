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

from pykerio.enums import ZeroConfigItemType


class TestCase_ZeroConfigItemType(unittest.TestCase):
    def test_00_ZeroConfigVpnClients(self):
        """
        Test ZeroConfigItemType with ZeroConfigVpnClients
        """
        value = ZeroConfigItemType.ZeroConfigVpnClients
        self.assertEqual(value.dump(), 'ZeroConfigVpnClients')
        self.assertEqual(value.name, 'ZeroConfigVpnClients')
        self.assertEqual(value.value, 0)

    def test_01_ZeroConfigVpnTunnel(self):
        """
        Test ZeroConfigItemType with ZeroConfigVpnTunnel
        """
        value = ZeroConfigItemType.ZeroConfigVpnTunnel
        self.assertEqual(value.dump(), 'ZeroConfigVpnTunnel')
        self.assertEqual(value.name, 'ZeroConfigVpnTunnel')
        self.assertEqual(value.value, 1)

    def test_02_ZeroConfigInterface(self):
        """
        Test ZeroConfigItemType with ZeroConfigInterface
        """
        value = ZeroConfigItemType.ZeroConfigInterface
        self.assertEqual(value.dump(), 'ZeroConfigInterface')
        self.assertEqual(value.name, 'ZeroConfigInterface')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ZeroConfigItemType with FAIL
        """
        value = ZeroConfigItemType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
