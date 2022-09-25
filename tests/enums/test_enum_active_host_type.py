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

from pykerio.enums import ActiveHostType


class TestCase_ActiveHostType(unittest.TestCase):
    def test_00_ActiveHostFirevall(self):
        """
        Test ActiveHostType with ActiveHostFirevall
        """
        value = ActiveHostType.ActiveHostFirevall
        self.assertEqual(value.dump(), 'ActiveHostFirevall')
        self.assertEqual(value.name, 'ActiveHostFirevall')
        self.assertEqual(value.value, 0)

    def test_01_ActiveHostVpnClient(self):
        """
        Test ActiveHostType with ActiveHostVpnClient
        """
        value = ActiveHostType.ActiveHostVpnClient
        self.assertEqual(value.dump(), 'ActiveHostVpnClient')
        self.assertEqual(value.name, 'ActiveHostVpnClient')
        self.assertEqual(value.value, 1)

    def test_02_ActiveHostHost(self):
        """
        Test ActiveHostType with ActiveHostHost
        """
        value = ActiveHostType.ActiveHostHost
        self.assertEqual(value.dump(), 'ActiveHostHost')
        self.assertEqual(value.name, 'ActiveHostHost')
        self.assertEqual(value.value, 2)

    def test_03_ActiveHostGuest(self):
        """
        Test ActiveHostType with ActiveHostGuest
        """
        value = ActiveHostType.ActiveHostGuest
        self.assertEqual(value.dump(), 'ActiveHostGuest')
        self.assertEqual(value.name, 'ActiveHostGuest')
        self.assertEqual(value.value, 3)
