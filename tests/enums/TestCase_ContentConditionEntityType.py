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


class TestCase_ContentConditionEntityType(unittest.TestCase):
    def test_00_ContentConditionEntityType_ContentConditionEntityApplication(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityApplication
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityApplication')
        self.assertEquals(value.dump(), 'ContentConditionEntityApplication')
        self.assertEquals(value.get_name(), 'ContentConditionEntityApplication')
        self.assertEquals(value.get_value(), 0)

    def test_01_ContentConditionEntityType_ContentConditionEntityFileName(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityFileName
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityFileName')
        self.assertEquals(value.dump(), 'ContentConditionEntityFileName')
        self.assertEquals(value.get_name(), 'ContentConditionEntityFileName')
        self.assertEquals(value.get_value(), 1)

    def test_02_ContentConditionEntityType_ContentConditionEntityFileGroup(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityFileGroup
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityFileGroup')
        self.assertEquals(value.dump(), 'ContentConditionEntityFileGroup')
        self.assertEquals(value.get_name(), 'ContentConditionEntityFileGroup')
        self.assertEquals(value.get_value(), 2)

    def test_03_ContentConditionEntityType_ContentConditionEntityUrl(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityUrl
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityUrl')
        self.assertEquals(value.dump(), 'ContentConditionEntityUrl')
        self.assertEquals(value.get_name(), 'ContentConditionEntityUrl')
        self.assertEquals(value.get_value(), 3)

    def test_04_ContentConditionEntityType_ContentConditionEntityUrlGroup(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityUrlGroup
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityUrlGroup')
        self.assertEquals(value.dump(), 'ContentConditionEntityUrlGroup')
        self.assertEquals(value.get_name(), 'ContentConditionEntityUrlGroup')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_ContentConditionEntityType_FAIL(self):
        """
        Test ContentConditionEntityType with FAIL
        """
        value = pykerio.enums.ContentConditionEntityType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
