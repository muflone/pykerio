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

from pykerio.enums import SourceNatMode


class TestCase_SourceNatMode(unittest.TestCase):
    def test_00_NatDefault(self):
        """
        Test SourceNatMode with NatDefault
        """
        value = SourceNatMode.NatDefault
        self.assertEqual(value.dump(), 'NatDefault')
        self.assertEqual(value.name, 'NatDefault')
        self.assertEqual(value.value, 0)

    def test_01_NatInterface(self):
        """
        Test SourceNatMode with NatInterface
        """
        value = SourceNatMode.NatInterface
        self.assertEqual(value.dump(), 'NatInterface')
        self.assertEqual(value.name, 'NatInterface')
        self.assertEqual(value.value, 1)

    def test_02_NatIpAddress(self):
        """
        Test SourceNatMode with NatIpAddress
        """
        value = SourceNatMode.NatIpAddress
        self.assertEqual(value.dump(), 'NatIpAddress')
        self.assertEqual(value.name, 'NatIpAddress')
        self.assertEqual(value.value, 2)
