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


class TestCase_ItemName(unittest.TestCase):
    def test_00_ItemName_Name(self):
        """
        Test ItemName with Name
        """
        value = pykerio.enums.ItemName(name='Name')
        self.assertEquals(value.dump(), 'Name')
        self.assertEquals(value.get_name(), 'Name')
        self.assertEquals(value.get_value(), 0)

    def test_01_ItemName_Description(self):
        """
        Test ItemName with Description
        """
        value = pykerio.enums.ItemName(name='Description')
        self.assertEquals(value.dump(), 'Description')
        self.assertEquals(value.get_name(), 'Description')
        self.assertEquals(value.get_value(), 1)

    def test_02_ItemName_Email(self):
        """
        Test ItemName with Email
        """
        value = pykerio.enums.ItemName(name='Email')
        self.assertEquals(value.dump(), 'Email')
        self.assertEquals(value.get_name(), 'Email')
        self.assertEquals(value.get_value(), 2)

    def test_03_ItemName_FullName(self):
        """
        Test ItemName with FullName
        """
        value = pykerio.enums.ItemName(name='FullName')
        self.assertEquals(value.dump(), 'FullName')
        self.assertEquals(value.get_name(), 'FullName')
        self.assertEquals(value.get_value(), 3)

    def test_04_ItemName_TimeItem(self):
        """
        Test ItemName with TimeItem
        """
        value = pykerio.enums.ItemName(name='TimeItem')
        self.assertEquals(value.dump(), 'TimeItem')
        self.assertEquals(value.get_name(), 'TimeItem')
        self.assertEquals(value.get_value(), 4)

    def test_05_ItemName_DateItem(self):
        """
        Test ItemName with DateItem
        """
        value = pykerio.enums.ItemName(name='DateItem')
        self.assertEquals(value.dump(), 'DateItem')
        self.assertEquals(value.get_name(), 'DateItem')
        self.assertEquals(value.get_value(), 5)

    def test_06_ItemName_DomainName(self):
        """
        Test ItemName with DomainName
        """
        value = pykerio.enums.ItemName(name='DomainName')
        self.assertEquals(value.dump(), 'DomainName')
        self.assertEquals(value.get_name(), 'DomainName')
        self.assertEquals(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_ItemName_FAIL(self):
        """
        Test ItemName with FAIL
        """
        value = pykerio.enums.ItemName(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
