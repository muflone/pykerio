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


class TestCase_BMConditionType(unittest.TestCase):
    def test_00_BMConditionType_BMConditionTrafficType(self):
        """
        Test BMConditionType with BMConditionTrafficType
        """
        value = pykerio.enums.BMConditionType(name='BMConditionTrafficType')
        self.assertEquals(value.dump(), 'BMConditionTrafficType')
        self.assertEquals(value.get_name(), 'BMConditionTrafficType')
        self.assertEquals(value.get_value(), 0)

    def test_01_BMConditionType_BMConditionQuota(self):
        """
        Test BMConditionType with BMConditionQuota
        """
        value = pykerio.enums.BMConditionType(name='BMConditionQuota')
        self.assertEquals(value.dump(), 'BMConditionQuota')
        self.assertEquals(value.get_name(), 'BMConditionQuota')
        self.assertEquals(value.get_value(), 1)

    def test_02_BMConditionType_BMConditionLargeData(self):
        """
        Test BMConditionType with BMConditionLargeData
        """
        value = pykerio.enums.BMConditionType(name='BMConditionLargeData')
        self.assertEquals(value.dump(), 'BMConditionLargeData')
        self.assertEquals(value.get_name(), 'BMConditionLargeData')
        self.assertEquals(value.get_value(), 2)

    def test_03_BMConditionType_BMConditionTrafficRule(self):
        """
        Test BMConditionType with BMConditionTrafficRule
        """
        value = pykerio.enums.BMConditionType(name='BMConditionTrafficRule')
        self.assertEquals(value.dump(), 'BMConditionTrafficRule')
        self.assertEquals(value.get_name(), 'BMConditionTrafficRule')
        self.assertEquals(value.get_value(), 3)

    def test_04_BMConditionType_BMConditionContentRule(self):
        """
        Test BMConditionType with BMConditionContentRule
        """
        value = pykerio.enums.BMConditionType(name='BMConditionContentRule')
        self.assertEquals(value.dump(), 'BMConditionContentRule')
        self.assertEquals(value.get_name(), 'BMConditionContentRule')
        self.assertEquals(value.get_value(), 4)

    def test_05_BMConditionType_BMConditionService(self):
        """
        Test BMConditionType with BMConditionService
        """
        value = pykerio.enums.BMConditionType(name='BMConditionService')
        self.assertEquals(value.dump(), 'BMConditionService')
        self.assertEquals(value.get_name(), 'BMConditionService')
        self.assertEquals(value.get_value(), 5)

    def test_06_BMConditionType_BMConditionDscp(self):
        """
        Test BMConditionType with BMConditionDscp
        """
        value = pykerio.enums.BMConditionType(name='BMConditionDscp')
        self.assertEquals(value.dump(), 'BMConditionDscp')
        self.assertEquals(value.get_name(), 'BMConditionDscp')
        self.assertEquals(value.get_value(), 6)

    def test_07_BMConditionType_BMConditionUsers(self):
        """
        Test BMConditionType with BMConditionUsers
        """
        value = pykerio.enums.BMConditionType(name='BMConditionUsers')
        self.assertEquals(value.dump(), 'BMConditionUsers')
        self.assertEquals(value.get_name(), 'BMConditionUsers')
        self.assertEquals(value.get_value(), 7)

    def test_08_BMConditionType_BMConditionInvalid(self):
        """
        Test BMConditionType with BMConditionInvalid
        """
        value = pykerio.enums.BMConditionType(name='BMConditionInvalid')
        self.assertEquals(value.dump(), 'BMConditionInvalid')
        self.assertEquals(value.get_name(), 'BMConditionInvalid')
        self.assertEquals(value.get_value(), 8)

    def test_09_BMConditionType_BMContentRuleType(self):
        """
        Test BMConditionType with BMContentRuleType
        """
        value = pykerio.enums.BMConditionType(name='BMContentRuleType')
        self.assertEquals(value.dump(), 'BMContentRuleType')
        self.assertEquals(value.get_name(), 'BMContentRuleType')
        self.assertEquals(value.get_value(), 9)

    def test_10_BMConditionType_BMConditionGuests(self):
        """
        Test BMConditionType with BMConditionGuests
        """
        value = pykerio.enums.BMConditionType(name='BMConditionGuests')
        self.assertEquals(value.dump(), 'BMConditionGuests')
        self.assertEquals(value.get_name(), 'BMConditionGuests')
        self.assertEquals(value.get_value(), 10)

    def test_11_BMConditionType_BMConditionApplication(self):
        """
        Test BMConditionType with BMConditionApplication
        """
        value = pykerio.enums.BMConditionType(name='BMConditionApplication')
        self.assertEquals(value.dump(), 'BMConditionApplication')
        self.assertEquals(value.get_name(), 'BMConditionApplication')
        self.assertEquals(value.get_value(), 11)

    @unittest.expectedFailure
    def test_99_BMConditionType_FAIL(self):
        """
        Test BMConditionType with FAIL
        """
        value = pykerio.enums.BMConditionType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
