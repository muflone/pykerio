##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
#   Copyright: 2018-2023 Fabio Castelli
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

from pykerio.enums import ValidType


class TestCase_ValidType(unittest.TestCase):
    def test_00_ValidType_Valid(self):
        """
        Test ValidType with Valid
        """
        value = ValidType.Valid
        self.assertEqual(value.dump(), 'Valid')
        self.assertEqual(value.name, 'Valid')
        self.assertEqual(value.value, 0)

    def test_01_ValidType_NotValidYet(self):
        """
        Test ValidType with NotValidYet
        """
        value = ValidType.NotValidYet
        self.assertEqual(value.dump(), 'NotValidYet')
        self.assertEqual(value.name, 'NotValidYet')
        self.assertEqual(value.value, 1)

    def test_02_ValidType_ExpireSoon(self):
        """
        Test ValidType with ExpireSoon
        """
        value = ValidType.ExpireSoon
        self.assertEqual(value.dump(), 'ExpireSoon')
        self.assertEqual(value.name, 'ExpireSoon')
        self.assertEqual(value.value, 2)

    def test_03_ValidType_Expired(self):
        """
        Test ValidType with Expired
        """
        value = ValidType.Expired
        self.assertEqual(value.dump(), 'Expired')
        self.assertEqual(value.name, 'Expired')
        self.assertEqual(value.value, 3)
