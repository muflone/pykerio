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


class TestCase_TrafficEntityType(unittest.TestCase):
    def test_00_TrafficEntityType_TrafficEntityHost(self):
        """
        Test TrafficEntityType with TrafficEntityHost
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityHost')
        self.assertEqual(value.dump(), 'TrafficEntityHost')
        self.assertEqual(value.get_name(), 'TrafficEntityHost')
        self.assertEqual(value.get_value(), 0)

    def test_01_TrafficEntityType_TrafficEntityNetwork(self):
        """
        Test TrafficEntityType with TrafficEntityNetwork
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityNetwork')
        self.assertEqual(value.dump(), 'TrafficEntityNetwork')
        self.assertEqual(value.get_name(), 'TrafficEntityNetwork')
        self.assertEqual(value.get_value(), 1)

    def test_02_TrafficEntityType_TrafficEntityRange(self):
        """
        Test TrafficEntityType with TrafficEntityRange
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityRange')
        self.assertEqual(value.dump(), 'TrafficEntityRange')
        self.assertEqual(value.get_name(), 'TrafficEntityRange')
        self.assertEqual(value.get_value(), 2)

    def test_03_TrafficEntityType_TrafficEntityAddressGroup(self):
        """
        Test TrafficEntityType with TrafficEntityAddressGroup
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityAddressGroup')
        self.assertEqual(value.dump(), 'TrafficEntityAddressGroup')
        self.assertEqual(value.get_name(), 'TrafficEntityAddressGroup')
        self.assertEqual(value.get_value(), 3)

    def test_04_TrafficEntityType_TrafficEntityPrefix(self):
        """
        Test TrafficEntityType with TrafficEntityPrefix
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityPrefix')
        self.assertEqual(value.dump(), 'TrafficEntityPrefix')
        self.assertEqual(value.get_name(), 'TrafficEntityPrefix')
        self.assertEqual(value.get_value(), 4)

    def test_05_TrafficEntityType_TrafficEntityInterface(self):
        """
        Test TrafficEntityType with TrafficEntityInterface
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityInterface')
        self.assertEqual(value.dump(), 'TrafficEntityInterface')
        self.assertEqual(value.get_name(), 'TrafficEntityInterface')
        self.assertEqual(value.get_value(), 5)

    def test_06_TrafficEntityType_TrafficEntityVpn(self):
        """
        Test TrafficEntityType with TrafficEntityVpn
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityVpn')
        self.assertEqual(value.dump(), 'TrafficEntityVpn')
        self.assertEqual(value.get_name(), 'TrafficEntityVpn')
        self.assertEqual(value.get_value(), 6)

    def test_07_TrafficEntityType_TrafficEntityUsers(self):
        """
        Test TrafficEntityType with TrafficEntityUsers
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityUsers')
        self.assertEqual(value.dump(), 'TrafficEntityUsers')
        self.assertEqual(value.get_name(), 'TrafficEntityUsers')
        self.assertEqual(value.get_value(), 7)

    @unittest.expectedFailure
    def test_99_TrafficEntityType_FAIL(self):
        """
        Test TrafficEntityType with FAIL
        """
        value = pykerio.enums.TrafficEntityType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
