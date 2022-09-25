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


class TestCase_ItemName(unittest.TestCase):
    def test_00_Name(self):
        """
        Test ItemName with Name
        """
        value = pykerio.enums.ItemName(name='Name')
        self.assertEqual(value.dump(), 'Name')
        self.assertEqual(value.get_name(), 'Name')
        self.assertEqual(value.get_value(), 0)

    def test_01_Description(self):
        """
        Test ItemName with Description
        """
        value = pykerio.enums.ItemName(name='Description')
        self.assertEqual(value.dump(), 'Description')
        self.assertEqual(value.get_name(), 'Description')
        self.assertEqual(value.get_value(), 1)

    def test_02_Email(self):
        """
        Test ItemName with Email
        """
        value = pykerio.enums.ItemName(name='Email')
        self.assertEqual(value.dump(), 'Email')
        self.assertEqual(value.get_name(), 'Email')
        self.assertEqual(value.get_value(), 2)

    def test_03_FullName(self):
        """
        Test ItemName with FullName
        """
        value = pykerio.enums.ItemName(name='FullName')
        self.assertEqual(value.dump(), 'FullName')
        self.assertEqual(value.get_name(), 'FullName')
        self.assertEqual(value.get_value(), 3)

    def test_04_TimeItem(self):
        """
        Test ItemName with TimeItem
        """
        value = pykerio.enums.ItemName(name='TimeItem')
        self.assertEqual(value.dump(), 'TimeItem')
        self.assertEqual(value.get_name(), 'TimeItem')
        self.assertEqual(value.get_value(), 4)

    def test_05_DateItem(self):
        """
        Test ItemName with DateItem
        """
        value = pykerio.enums.ItemName(name='DateItem')
        self.assertEqual(value.dump(), 'DateItem')
        self.assertEqual(value.get_name(), 'DateItem')
        self.assertEqual(value.get_value(), 5)

    def test_06_DomainName(self):
        """
        Test ItemName with DomainName
        """
        value = pykerio.enums.ItemName(name='DomainName')
        self.assertEqual(value.dump(), 'DomainName')
        self.assertEqual(value.get_name(), 'DomainName')
        self.assertEqual(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ItemName with FAIL
        """
        value = pykerio.enums.ItemName(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
