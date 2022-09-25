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


class TestCase_InterfaceType(unittest.TestCase):
    def test_00_Ethernet(self):
        """
        Test InterfaceType with Ethernet
        """
        value = pykerio.enums.InterfaceType(name='Ethernet')
        self.assertEqual(value.dump(), 'Ethernet')
        self.assertEqual(value.get_name(), 'Ethernet')
        self.assertEqual(value.get_value(), 0)

    def test_01_Ras(self):
        """
        Test InterfaceType with Ras
        """
        value = pykerio.enums.InterfaceType(name='Ras')
        self.assertEqual(value.dump(), 'Ras')
        self.assertEqual(value.get_name(), 'Ras')
        self.assertEqual(value.get_value(), 1)

    def test_02_DialIn(self):
        """
        Test InterfaceType with DialIn
        """
        value = pykerio.enums.InterfaceType(name='DialIn')
        self.assertEqual(value.dump(), 'DialIn')
        self.assertEqual(value.get_name(), 'DialIn')
        self.assertEqual(value.get_value(), 2)

    def test_03_VpnServer(self):
        """
        Test InterfaceType with VpnServer
        """
        value = pykerio.enums.InterfaceType(name='VpnServer')
        self.assertEqual(value.dump(), 'VpnServer')
        self.assertEqual(value.get_name(), 'VpnServer')
        self.assertEqual(value.get_value(), 3)

    def test_04_VpnTunnel(self):
        """
        Test InterfaceType with VpnTunnel
        """
        value = pykerio.enums.InterfaceType(name='VpnTunnel')
        self.assertEqual(value.dump(), 'VpnTunnel')
        self.assertEqual(value.get_name(), 'VpnTunnel')
        self.assertEqual(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test InterfaceType with FAIL
        """
        value = pykerio.enums.InterfaceType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
