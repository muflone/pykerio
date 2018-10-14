##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import unittest

import pykerio


class TestCase_TrafficEntityType(unittest.TestCase):
    def test_00_TrafficEntityType_TrafficEntityHost(self):
        """
        Test TrafficEntityType with TrafficEntityHost
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityHost')
        self.assertEquals(value.dump(), 'TrafficEntityHost')
        self.assertEquals(value.get_name(), 'TrafficEntityHost')
        self.assertEquals(value.get_value(), 0)

    def test_01_TrafficEntityType_TrafficEntityNetwork(self):
        """
        Test TrafficEntityType with TrafficEntityNetwork
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityNetwork')
        self.assertEquals(value.dump(), 'TrafficEntityNetwork')
        self.assertEquals(value.get_name(), 'TrafficEntityNetwork')
        self.assertEquals(value.get_value(), 1)

    def test_02_TrafficEntityType_TrafficEntityRange(self):
        """
        Test TrafficEntityType with TrafficEntityRange
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityRange')
        self.assertEquals(value.dump(), 'TrafficEntityRange')
        self.assertEquals(value.get_name(), 'TrafficEntityRange')
        self.assertEquals(value.get_value(), 2)

    def test_03_TrafficEntityType_TrafficEntityAddressGroup(self):
        """
        Test TrafficEntityType with TrafficEntityAddressGroup
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityAddressGroup')
        self.assertEquals(value.dump(), 'TrafficEntityAddressGroup')
        self.assertEquals(value.get_name(), 'TrafficEntityAddressGroup')
        self.assertEquals(value.get_value(), 3)

    def test_04_TrafficEntityType_TrafficEntityPrefix(self):
        """
        Test TrafficEntityType with TrafficEntityPrefix
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityPrefix')
        self.assertEquals(value.dump(), 'TrafficEntityPrefix')
        self.assertEquals(value.get_name(), 'TrafficEntityPrefix')
        self.assertEquals(value.get_value(), 4)

    def test_05_TrafficEntityType_TrafficEntityInterface(self):
        """
        Test TrafficEntityType with TrafficEntityInterface
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityInterface')
        self.assertEquals(value.dump(), 'TrafficEntityInterface')
        self.assertEquals(value.get_name(), 'TrafficEntityInterface')
        self.assertEquals(value.get_value(), 5)

    def test_06_TrafficEntityType_TrafficEntityVpn(self):
        """
        Test TrafficEntityType with TrafficEntityVpn
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityVpn')
        self.assertEquals(value.dump(), 'TrafficEntityVpn')
        self.assertEquals(value.get_name(), 'TrafficEntityVpn')
        self.assertEquals(value.get_value(), 6)

    def test_07_TrafficEntityType_TrafficEntityUsers(self):
        """
        Test TrafficEntityType with TrafficEntityUsers
        """
        value = pykerio.enums.TrafficEntityType(name='TrafficEntityUsers')
        self.assertEquals(value.dump(), 'TrafficEntityUsers')
        self.assertEquals(value.get_name(), 'TrafficEntityUsers')
        self.assertEquals(value.get_value(), 7)

    @unittest.expectedFailure
    def test_99_TrafficEntityType_FAIL(self):
        """
        Test TrafficEntityType with FAIL
        """
        value = pykerio.enums.TrafficEntityType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
