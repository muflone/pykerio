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

from pykerio.enums import TrafficEntityType


class TestCase_TrafficEntityType(unittest.TestCase):
    def test_00_TrafficEntityHost(self):
        """
        Test TrafficEntityType with TrafficEntityHost
        """
        value = TrafficEntityType.TrafficEntityHost
        self.assertEqual(value.dump(), 'TrafficEntityHost')
        self.assertEqual(value.name, 'TrafficEntityHost')
        self.assertEqual(value.value, 0)

    def test_01_TrafficEntityNetwork(self):
        """
        Test TrafficEntityType with TrafficEntityNetwork
        """
        value = TrafficEntityType.TrafficEntityNetwork
        self.assertEqual(value.dump(), 'TrafficEntityNetwork')
        self.assertEqual(value.name, 'TrafficEntityNetwork')
        self.assertEqual(value.value, 1)

    def test_02_TrafficEntityRange(self):
        """
        Test TrafficEntityType with TrafficEntityRange
        """
        value = TrafficEntityType.TrafficEntityRange
        self.assertEqual(value.dump(), 'TrafficEntityRange')
        self.assertEqual(value.name, 'TrafficEntityRange')
        self.assertEqual(value.value, 2)

    def test_03_TrafficEntityAddressGroup(self):
        """
        Test TrafficEntityType with TrafficEntityAddressGroup
        """
        value = TrafficEntityType.TrafficEntityAddressGroup
        self.assertEqual(value.dump(), 'TrafficEntityAddressGroup')
        self.assertEqual(value.name, 'TrafficEntityAddressGroup')
        self.assertEqual(value.value, 3)

    def test_04_TrafficEntityPrefix(self):
        """
        Test TrafficEntityType with TrafficEntityPrefix
        """
        value = TrafficEntityType.TrafficEntityPrefix
        self.assertEqual(value.dump(), 'TrafficEntityPrefix')
        self.assertEqual(value.name, 'TrafficEntityPrefix')
        self.assertEqual(value.value, 4)

    def test_05_TrafficEntityInterface(self):
        """
        Test TrafficEntityType with TrafficEntityInterface
        """
        value = TrafficEntityType.TrafficEntityInterface
        self.assertEqual(value.dump(), 'TrafficEntityInterface')
        self.assertEqual(value.name, 'TrafficEntityInterface')
        self.assertEqual(value.value, 5)

    def test_06_TrafficEntityVpn(self):
        """
        Test TrafficEntityType with TrafficEntityVpn
        """
        value = TrafficEntityType.TrafficEntityVpn
        self.assertEqual(value.dump(), 'TrafficEntityVpn')
        self.assertEqual(value.name, 'TrafficEntityVpn')
        self.assertEqual(value.value, 6)

    def test_07_TrafficEntityUsers(self):
        """
        Test TrafficEntityType with TrafficEntityUsers
        """
        value = TrafficEntityType.TrafficEntityUsers
        self.assertEqual(value.dump(), 'TrafficEntityUsers')
        self.assertEqual(value.name, 'TrafficEntityUsers')
        self.assertEqual(value.value, 7)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test TrafficEntityType with FAIL
        """
        value = TrafficEntityType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
