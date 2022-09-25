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

from pykerio.enums import UserFormatType


class TestCase_UserFormatType(unittest.TestCase):
    def test_00_UserFormatFL(self):
        """
        Test UserFormatType with UserFormatFL
        """
        value = UserFormatType.UserFormatFL
        self.assertEqual(value.dump(), 'UserFormatFL')
        self.assertEqual(value.name, 'UserFormatFL')
        self.assertEqual(value.value, 0)

    def test_01_UserFormatFLU(self):
        """
        Test UserFormatType with UserFormatFLU
        """
        value = UserFormatType.UserFormatFLU
        self.assertEqual(value.dump(), 'UserFormatFLU')
        self.assertEqual(value.name, 'UserFormatFLU')
        self.assertEqual(value.value, 1)

    def test_02_UserFormatFLD(self):
        """
        Test UserFormatType with UserFormatFLD
        """
        value = UserFormatType.UserFormatFLD
        self.assertEqual(value.dump(), 'UserFormatFLD')
        self.assertEqual(value.name, 'UserFormatFLD')
        self.assertEqual(value.value, 2)

    def test_03_UserFormatLF(self):
        """
        Test UserFormatType with UserFormatLF
        """
        value = UserFormatType.UserFormatLF
        self.assertEqual(value.dump(), 'UserFormatLF')
        self.assertEqual(value.name, 'UserFormatLF')
        self.assertEqual(value.value, 3)

    def test_04_UserFormatLFU(self):
        """
        Test UserFormatType with UserFormatLFU
        """
        value = UserFormatType.UserFormatLFU
        self.assertEqual(value.dump(), 'UserFormatLFU')
        self.assertEqual(value.name, 'UserFormatLFU')
        self.assertEqual(value.value, 4)

    def test_05_UserFormatLFD(self):
        """
        Test UserFormatType with UserFormatLFD
        """
        value = UserFormatType.UserFormatLFD
        self.assertEqual(value.dump(), 'UserFormatLFD')
        self.assertEqual(value.name, 'UserFormatLFD')
        self.assertEqual(value.value, 5)
