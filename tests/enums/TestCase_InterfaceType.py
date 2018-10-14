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


class TestCase_InterfaceType(unittest.TestCase):
    def test_00_InterfaceType_Ethernet(self):
        """
        Test InterfaceType with Ethernet
        """
        value = pykerio.enums.InterfaceType(name='Ethernet')
        self.assertEquals(value.dump(), 'Ethernet')
        self.assertEquals(value.get_name(), 'Ethernet')
        self.assertEquals(value.get_value(), 0)

    def test_01_InterfaceType_Ras(self):
        """
        Test InterfaceType with Ras
        """
        value = pykerio.enums.InterfaceType(name='Ras')
        self.assertEquals(value.dump(), 'Ras')
        self.assertEquals(value.get_name(), 'Ras')
        self.assertEquals(value.get_value(), 1)

    def test_02_InterfaceType_DialIn(self):
        """
        Test InterfaceType with DialIn
        """
        value = pykerio.enums.InterfaceType(name='DialIn')
        self.assertEquals(value.dump(), 'DialIn')
        self.assertEquals(value.get_name(), 'DialIn')
        self.assertEquals(value.get_value(), 2)

    def test_03_InterfaceType_VpnServer(self):
        """
        Test InterfaceType with VpnServer
        """
        value = pykerio.enums.InterfaceType(name='VpnServer')
        self.assertEquals(value.dump(), 'VpnServer')
        self.assertEquals(value.get_name(), 'VpnServer')
        self.assertEquals(value.get_value(), 3)

    def test_04_InterfaceType_VpnTunnel(self):
        """
        Test InterfaceType with VpnTunnel
        """
        value = pykerio.enums.InterfaceType(name='VpnTunnel')
        self.assertEquals(value.dump(), 'VpnTunnel')
        self.assertEquals(value.get_name(), 'VpnTunnel')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_InterfaceType_FAIL(self):
        """
        Test InterfaceType with FAIL
        """
        value = pykerio.enums.InterfaceType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
