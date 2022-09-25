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

from pykerio.enums import ItemName


class TestCase_ItemName(unittest.TestCase):
    def test_00_Name(self):
        """
        Test ItemName with Name
        """
        value = ItemName.Name
        self.assertEqual(value.dump(), 'Name')
        self.assertEqual(value.name, 'Name')
        self.assertEqual(value.value, 0)

    def test_01_Description(self):
        """
        Test ItemName with Description
        """
        value = ItemName.Description
        self.assertEqual(value.dump(), 'Description')
        self.assertEqual(value.name, 'Description')
        self.assertEqual(value.value, 1)

    def test_02_Email(self):
        """
        Test ItemName with Email
        """
        value = ItemName.Email
        self.assertEqual(value.dump(), 'Email')
        self.assertEqual(value.name, 'Email')
        self.assertEqual(value.value, 2)

    def test_03_FullName(self):
        """
        Test ItemName with FullName
        """
        value = ItemName.FullName
        self.assertEqual(value.dump(), 'FullName')
        self.assertEqual(value.name, 'FullName')
        self.assertEqual(value.value, 3)

    def test_04_TimeItem(self):
        """
        Test ItemName with TimeItem
        """
        value = ItemName.TimeItem
        self.assertEqual(value.dump(), 'TimeItem')
        self.assertEqual(value.name, 'TimeItem')
        self.assertEqual(value.value, 4)

    def test_05_DateItem(self):
        """
        Test ItemName with DateItem
        """
        value = ItemName.DateItem
        self.assertEqual(value.dump(), 'DateItem')
        self.assertEqual(value.name, 'DateItem')
        self.assertEqual(value.value, 5)

    def test_06_DomainName(self):
        """
        Test ItemName with DomainName
        """
        value = ItemName.DomainName
        self.assertEqual(value.dump(), 'DomainName')
        self.assertEqual(value.name, 'DomainName')
        self.assertEqual(value.value, 6)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ItemName with FAIL
        """
        value = ItemName.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
