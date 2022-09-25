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


class TestCase_ContentConditionEntityType(unittest.TestCase):
    def test_00_ContentConditionEntityApplication(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityApplication
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityApplication')
        self.assertEqual(value.dump(), 'ContentConditionEntityApplication')
        self.assertEqual(value.get_name(), 'ContentConditionEntityApplication')
        self.assertEqual(value.get_value(), 0)

    def test_01_ContentConditionEntityFileName(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityFileName
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityFileName')
        self.assertEqual(value.dump(), 'ContentConditionEntityFileName')
        self.assertEqual(value.get_name(), 'ContentConditionEntityFileName')
        self.assertEqual(value.get_value(), 1)

    def test_02_ContentConditionEntityFileGroup(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityFileGroup
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityFileGroup')
        self.assertEqual(value.dump(), 'ContentConditionEntityFileGroup')
        self.assertEqual(value.get_name(), 'ContentConditionEntityFileGroup')
        self.assertEqual(value.get_value(), 2)

    def test_03_ContentConditionEntityUrl(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityUrl
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityUrl')
        self.assertEqual(value.dump(), 'ContentConditionEntityUrl')
        self.assertEqual(value.get_name(), 'ContentConditionEntityUrl')
        self.assertEqual(value.get_value(), 3)

    def test_04_ContentConditionEntityUrlGroup(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityUrlGroup
        """
        value = pykerio.enums.ContentConditionEntityType(name='ContentConditionEntityUrlGroup')
        self.assertEqual(value.dump(), 'ContentConditionEntityUrlGroup')
        self.assertEqual(value.get_name(), 'ContentConditionEntityUrlGroup')
        self.assertEqual(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ContentConditionEntityType with FAIL
        """
        value = pykerio.enums.ContentConditionEntityType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
