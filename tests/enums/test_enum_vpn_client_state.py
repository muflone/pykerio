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

from pykerio.enums import VpnClientState


class TestCase_VpnClientState(unittest.TestCase):
    def test_00_VpnClientConnecting(self):
        """
        Test VpnClientState with VpnClientConnecting
        """
        value = VpnClientState.VpnClientConnecting
        self.assertEqual(value.dump(), 'VpnClientConnecting')
        self.assertEqual(value.name, 'VpnClientConnecting')
        self.assertEqual(value.value, 0)

    def test_01_VpnClientAuthenticating(self):
        """
        Test VpnClientState with VpnClientAuthenticating
        """
        value = VpnClientState.VpnClientAuthenticating
        self.assertEqual(value.dump(), 'VpnClientAuthenticating')
        self.assertEqual(value.name, 'VpnClientAuthenticating')
        self.assertEqual(value.value, 1)

    def test_02_VpnClientAuthenticated(self):
        """
        Test VpnClientState with VpnClientAuthenticated
        """
        value = VpnClientState.VpnClientAuthenticated
        self.assertEqual(value.dump(), 'VpnClientAuthenticated')
        self.assertEqual(value.name, 'VpnClientAuthenticated')
        self.assertEqual(value.value, 2)

    def test_03_VpnClientConnected(self):
        """
        Test VpnClientState with VpnClientConnected
        """
        value = VpnClientState.VpnClientConnected
        self.assertEqual(value.dump(), 'VpnClientConnected')
        self.assertEqual(value.name, 'VpnClientConnected')
        self.assertEqual(value.value, 3)

    def test_04_VpnClientOther(self):
        """
        Test VpnClientState with VpnClientOther
        """
        value = VpnClientState.VpnClientOther
        self.assertEqual(value.dump(), 'VpnClientOther')
        self.assertEqual(value.name, 'VpnClientOther')
        self.assertEqual(value.value, 4)
