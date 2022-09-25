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

from pykerio.enums import ContentConditionEntityType


class TestCase_ContentConditionEntityType(unittest.TestCase):
    def test_00_ContentConditionEntityApplication(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityApplication
        """
        value = ContentConditionEntityType.ContentConditionEntityApplication
        self.assertEqual(value.dump(), 'ContentConditionEntityApplication')
        self.assertEqual(value.name, 'ContentConditionEntityApplication')
        self.assertEqual(value.value, 0)

    def test_01_ContentConditionEntityFileName(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityFileName
        """
        value = ContentConditionEntityType.ContentConditionEntityFileName
        self.assertEqual(value.dump(), 'ContentConditionEntityFileName')
        self.assertEqual(value.name, 'ContentConditionEntityFileName')
        self.assertEqual(value.value, 1)

    def test_02_ContentConditionEntityFileGroup(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityFileGroup
        """
        value = ContentConditionEntityType.ContentConditionEntityFileGroup
        self.assertEqual(value.dump(), 'ContentConditionEntityFileGroup')
        self.assertEqual(value.name, 'ContentConditionEntityFileGroup')
        self.assertEqual(value.value, 2)

    def test_03_ContentConditionEntityUrl(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityUrl
        """
        value = ContentConditionEntityType.ContentConditionEntityUrl
        self.assertEqual(value.dump(), 'ContentConditionEntityUrl')
        self.assertEqual(value.name, 'ContentConditionEntityUrl')
        self.assertEqual(value.value, 3)

    def test_04_ContentConditionEntityUrlGroup(self):
        """
        Test ContentConditionEntityType with ContentConditionEntityUrlGroup
        """
        value = ContentConditionEntityType.ContentConditionEntityUrlGroup
        self.assertEqual(value.dump(), 'ContentConditionEntityUrlGroup')
        self.assertEqual(value.name, 'ContentConditionEntityUrlGroup')
        self.assertEqual(value.value, 4)
