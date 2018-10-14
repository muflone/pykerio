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


class TestCase_ZeroConfigItemType(unittest.TestCase):
    def test_00_ZeroConfigItemType_ZeroConfigVpnClients(self):
        """
        Test ZeroConfigItemType with ZeroConfigVpnClients
        """
        value = pykerio.enums.ZeroConfigItemType(name='ZeroConfigVpnClients')
        self.assertEquals(value.dump(), 'ZeroConfigVpnClients')
        self.assertEquals(value.get_name(), 'ZeroConfigVpnClients')
        self.assertEquals(value.get_value(), 0)

    def test_01_ZeroConfigItemType_ZeroConfigVpnTunnel(self):
        """
        Test ZeroConfigItemType with ZeroConfigVpnTunnel
        """
        value = pykerio.enums.ZeroConfigItemType(name='ZeroConfigVpnTunnel')
        self.assertEquals(value.dump(), 'ZeroConfigVpnTunnel')
        self.assertEquals(value.get_name(), 'ZeroConfigVpnTunnel')
        self.assertEquals(value.get_value(), 1)

    def test_02_ZeroConfigItemType_ZeroConfigInterface(self):
        """
        Test ZeroConfigItemType with ZeroConfigInterface
        """
        value = pykerio.enums.ZeroConfigItemType(name='ZeroConfigInterface')
        self.assertEquals(value.dump(), 'ZeroConfigInterface')
        self.assertEquals(value.get_name(), 'ZeroConfigInterface')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_ZeroConfigItemType_FAIL(self):
        """
        Test ZeroConfigItemType with FAIL
        """
        value = pykerio.enums.ZeroConfigItemType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
