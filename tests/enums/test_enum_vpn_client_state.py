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


class TestCase_VpnClientState(unittest.TestCase):
    def test_00_VpnClientConnecting(self):
        """
        Test VpnClientState with VpnClientConnecting
        """
        value = pykerio.enums.VpnClientState(name='VpnClientConnecting')
        self.assertEqual(value.dump(), 'VpnClientConnecting')
        self.assertEqual(value.get_name(), 'VpnClientConnecting')
        self.assertEqual(value.get_value(), 0)

    def test_01_VpnClientAuthenticating(self):
        """
        Test VpnClientState with VpnClientAuthenticating
        """
        value = pykerio.enums.VpnClientState(name='VpnClientAuthenticating')
        self.assertEqual(value.dump(), 'VpnClientAuthenticating')
        self.assertEqual(value.get_name(), 'VpnClientAuthenticating')
        self.assertEqual(value.get_value(), 1)

    def test_02_VpnClientAuthenticated(self):
        """
        Test VpnClientState with VpnClientAuthenticated
        """
        value = pykerio.enums.VpnClientState(name='VpnClientAuthenticated')
        self.assertEqual(value.dump(), 'VpnClientAuthenticated')
        self.assertEqual(value.get_name(), 'VpnClientAuthenticated')
        self.assertEqual(value.get_value(), 2)

    def test_03_VpnClientConnected(self):
        """
        Test VpnClientState with VpnClientConnected
        """
        value = pykerio.enums.VpnClientState(name='VpnClientConnected')
        self.assertEqual(value.dump(), 'VpnClientConnected')
        self.assertEqual(value.get_name(), 'VpnClientConnected')
        self.assertEqual(value.get_value(), 3)

    def test_04_VpnClientOther(self):
        """
        Test VpnClientState with VpnClientOther
        """
        value = pykerio.enums.VpnClientState(name='VpnClientOther')
        self.assertEqual(value.dump(), 'VpnClientOther')
        self.assertEqual(value.get_name(), 'VpnClientOther')
        self.assertEqual(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test VpnClientState with FAIL
        """
        value = pykerio.enums.VpnClientState(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
