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

from pykerio.enums import BMConditionType


class TestCase_BMConditionType(unittest.TestCase):
    def test_00_BMConditionTrafficType(self):
        """
        Test BMConditionType with BMConditionTrafficType
        """
        value = BMConditionType.BMConditionTrafficType
        self.assertEqual(value.dump(), 'BMConditionTrafficType')
        self.assertEqual(value.name, 'BMConditionTrafficType')
        self.assertEqual(value.value, 0)

    def test_01_BMConditionQuota(self):
        """
        Test BMConditionType with BMConditionQuota
        """
        value = BMConditionType.BMConditionQuota
        self.assertEqual(value.dump(), 'BMConditionQuota')
        self.assertEqual(value.name, 'BMConditionQuota')
        self.assertEqual(value.value, 1)

    def test_02_BMConditionLargeData(self):
        """
        Test BMConditionType with BMConditionLargeData
        """
        value = BMConditionType.BMConditionLargeData
        self.assertEqual(value.dump(), 'BMConditionLargeData')
        self.assertEqual(value.name, 'BMConditionLargeData')
        self.assertEqual(value.value, 2)

    def test_03_BMConditionTrafficRule(self):
        """
        Test BMConditionType with BMConditionTrafficRule
        """
        value = BMConditionType.BMConditionTrafficRule
        self.assertEqual(value.dump(), 'BMConditionTrafficRule')
        self.assertEqual(value.name, 'BMConditionTrafficRule')
        self.assertEqual(value.value, 3)

    def test_04_BMConditionContentRule(self):
        """
        Test BMConditionType with BMConditionContentRule
        """
        value = BMConditionType.BMConditionContentRule
        self.assertEqual(value.dump(), 'BMConditionContentRule')
        self.assertEqual(value.name, 'BMConditionContentRule')
        self.assertEqual(value.value, 4)

    def test_05_BMConditionService(self):
        """
        Test BMConditionType with BMConditionService
        """
        value = BMConditionType.BMConditionService
        self.assertEqual(value.dump(), 'BMConditionService')
        self.assertEqual(value.name, 'BMConditionService')
        self.assertEqual(value.value, 5)

    def test_06_BMConditionDscp(self):
        """
        Test BMConditionType with BMConditionDscp
        """
        value = BMConditionType.BMConditionDscp
        self.assertEqual(value.dump(), 'BMConditionDscp')
        self.assertEqual(value.name, 'BMConditionDscp')
        self.assertEqual(value.value, 6)

    def test_07_BMConditionUsers(self):
        """
        Test BMConditionType with BMConditionUsers
        """
        value = BMConditionType.BMConditionUsers
        self.assertEqual(value.dump(), 'BMConditionUsers')
        self.assertEqual(value.name, 'BMConditionUsers')
        self.assertEqual(value.value, 7)

    def test_08_BMConditionInvalid(self):
        """
        Test BMConditionType with BMConditionInvalid
        """
        value = BMConditionType.BMConditionInvalid
        self.assertEqual(value.dump(), 'BMConditionInvalid')
        self.assertEqual(value.name, 'BMConditionInvalid')
        self.assertEqual(value.value, 8)

    def test_09_BMContentRuleType(self):
        """
        Test BMConditionType with BMContentRuleType
        """
        value = BMConditionType.BMContentRuleType
        self.assertEqual(value.dump(), 'BMContentRuleType')
        self.assertEqual(value.name, 'BMContentRuleType')
        self.assertEqual(value.value, 9)

    def test_10_BMConditionGuests(self):
        """
        Test BMConditionType with BMConditionGuests
        """
        value = BMConditionType.BMConditionGuests
        self.assertEqual(value.dump(), 'BMConditionGuests')
        self.assertEqual(value.name, 'BMConditionGuests')
        self.assertEqual(value.value, 10)

    def test_11_BMConditionApplication(self):
        """
        Test BMConditionType with BMConditionApplication
        """
        value = BMConditionType.BMConditionApplication
        self.assertEqual(value.dump(), 'BMConditionApplication')
        self.assertEqual(value.name, 'BMConditionApplication')
        self.assertEqual(value.value, 11)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test BMConditionType with FAIL
        """
        value = BMConditionType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
