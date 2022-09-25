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

from pykerio.enums import OsCodeType


class TestCase_OsCodeType(unittest.TestCase):
    def test_00_OsWindows(self):
        """
        Test OsCodeType with OsWindows
        """
        value = OsCodeType.OsWindows
        self.assertEqual(value.dump(), 'OsWindows')
        self.assertEqual(value.name, 'OsWindows')
        self.assertEqual(value.value, 0)

    def test_01_OsLinux(self):
        """
        Test OsCodeType with OsLinux
        """
        value = OsCodeType.OsLinux
        self.assertEqual(value.dump(), 'OsLinux')
        self.assertEqual(value.name, 'OsLinux')
        self.assertEqual(value.value, 1)

    def test_02_OsMacos(self):
        """
        Test OsCodeType with OsMacos
        """
        value = OsCodeType.OsMacos
        self.assertEqual(value.dump(), 'OsMacos')
        self.assertEqual(value.name, 'OsMacos')
        self.assertEqual(value.value, 2)

    def test_03_OsUnknown(self):
        """
        Test OsCodeType with OsUnknown
        """
        value = OsCodeType.OsUnknown
        self.assertEqual(value.dump(), 'OsUnknown')
        self.assertEqual(value.name, 'OsUnknown')
        self.assertEqual(value.value, 3)
