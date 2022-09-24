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


class TestCase_RuleConditionType(unittest.TestCase):
    def test_00_RuleConditionType_RuleAny(self):
        """
        Test RuleConditionType with RuleAny
        """
        value = pykerio.enums.RuleConditionType(name='RuleAny')
        self.assertEqual(value.dump(), 'RuleAny')
        self.assertEqual(value.get_name(), 'RuleAny')
        self.assertEqual(value.get_value(), 0)

    def test_01_RuleConditionType_RuleSelectedEntities(self):
        """
        Test RuleConditionType with RuleSelectedEntities
        """
        value = pykerio.enums.RuleConditionType(name='RuleSelectedEntities')
        self.assertEqual(value.dump(), 'RuleSelectedEntities')
        self.assertEqual(value.get_name(), 'RuleSelectedEntities')
        self.assertEqual(value.get_value(), 1)

    def test_02_RuleConditionType_RuleInvalidCondition(self):
        """
        Test RuleConditionType with RuleInvalidCondition
        """
        value = pykerio.enums.RuleConditionType(name='RuleInvalidCondition')
        self.assertEqual(value.dump(), 'RuleInvalidCondition')
        self.assertEqual(value.get_name(), 'RuleInvalidCondition')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_RuleConditionType_FAIL(self):
        """
        Test RuleConditionType with FAIL
        """
        value = pykerio.enums.RuleConditionType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
