##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
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


class TestCase_ValidType(unittest.TestCase):
    def test_00_ValidType_Valid(self):
        """
        Test ValidType with Valid
        """
        value = pykerio.enums.ValidType(name='Valid')
        self.assertEquals(value.dump(), 'Valid')
        self.assertEquals(value.get_name(), 'Valid')
        self.assertEquals(value.get_value(), 0)

    def test_01_ValidType_NotValidYet(self):
        """
        Test ValidType with NotValidYet
        """
        value = pykerio.enums.ValidType(name='NotValidYet')
        self.assertEquals(value.dump(), 'NotValidYet')
        self.assertEquals(value.get_name(), 'NotValidYet')
        self.assertEquals(value.get_value(), 1)

    def test_02_ValidType_ExpireSoon(self):
        """
        Test ValidType with ExpireSoon
        """
        value = pykerio.enums.ValidType(name='ExpireSoon')
        self.assertEquals(value.dump(), 'ExpireSoon')
        self.assertEquals(value.get_name(), 'ExpireSoon')
        self.assertEquals(value.get_value(), 2)

    def test_03_ValidType_Expired(self):
        """
        Test ValidType with Expired
        """
        value = pykerio.enums.ValidType(name='Expired')
        self.assertEquals(value.dump(), 'Expired')
        self.assertEquals(value.get_name(), 'Expired')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_ValidType_FAIL(self):
        """
        Test ValidType with FAIL
        """
        value = pykerio.enums.ValidType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
