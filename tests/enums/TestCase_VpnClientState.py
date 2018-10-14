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


class TestCase_VpnClientState(unittest.TestCase):
    def test_00_VpnClientState_VpnClientConnecting(self):
        """
        Test VpnClientState with VpnClientConnecting
        """
        value = pykerio.enums.VpnClientState(name='VpnClientConnecting')
        self.assertEquals(value.dump(), 'VpnClientConnecting')
        self.assertEquals(value.get_name(), 'VpnClientConnecting')
        self.assertEquals(value.get_value(), 0)

    def test_01_VpnClientState_VpnClientAuthenticating(self):
        """
        Test VpnClientState with VpnClientAuthenticating
        """
        value = pykerio.enums.VpnClientState(name='VpnClientAuthenticating')
        self.assertEquals(value.dump(), 'VpnClientAuthenticating')
        self.assertEquals(value.get_name(), 'VpnClientAuthenticating')
        self.assertEquals(value.get_value(), 1)

    def test_02_VpnClientState_VpnClientAuthenticated(self):
        """
        Test VpnClientState with VpnClientAuthenticated
        """
        value = pykerio.enums.VpnClientState(name='VpnClientAuthenticated')
        self.assertEquals(value.dump(), 'VpnClientAuthenticated')
        self.assertEquals(value.get_name(), 'VpnClientAuthenticated')
        self.assertEquals(value.get_value(), 2)

    def test_03_VpnClientState_VpnClientConnected(self):
        """
        Test VpnClientState with VpnClientConnected
        """
        value = pykerio.enums.VpnClientState(name='VpnClientConnected')
        self.assertEquals(value.dump(), 'VpnClientConnected')
        self.assertEquals(value.get_name(), 'VpnClientConnected')
        self.assertEquals(value.get_value(), 3)

    def test_04_VpnClientState_VpnClientOther(self):
        """
        Test VpnClientState with VpnClientOther
        """
        value = pykerio.enums.VpnClientState(name='VpnClientOther')
        self.assertEquals(value.dump(), 'VpnClientOther')
        self.assertEquals(value.get_name(), 'VpnClientOther')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_VpnClientState_FAIL(self):
        """
        Test VpnClientState with FAIL
        """
        value = pykerio.enums.VpnClientState(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
