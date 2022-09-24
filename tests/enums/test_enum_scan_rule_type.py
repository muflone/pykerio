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


class TestCase_ScanRuleType(unittest.TestCase):
    def test_00_ScanRuleType_ScanRuleUrl(self):
        """
        Test ScanRuleType with ScanRuleUrl
        """
        value = pykerio.enums.ScanRuleType(name='ScanRuleUrl')
        self.assertEqual(value.dump(), 'ScanRuleUrl')
        self.assertEqual(value.get_name(), 'ScanRuleUrl')
        self.assertEqual(value.get_value(), 0)

    def test_01_ScanRuleType_ScanRuleMime(self):
        """
        Test ScanRuleType with ScanRuleMime
        """
        value = pykerio.enums.ScanRuleType(name='ScanRuleMime')
        self.assertEqual(value.dump(), 'ScanRuleMime')
        self.assertEqual(value.get_name(), 'ScanRuleMime')
        self.assertEqual(value.get_value(), 1)

    def test_02_ScanRuleType_ScanRuleFilename(self):
        """
        Test ScanRuleType with ScanRuleFilename
        """
        value = pykerio.enums.ScanRuleType(name='ScanRuleFilename')
        self.assertEqual(value.dump(), 'ScanRuleFilename')
        self.assertEqual(value.get_name(), 'ScanRuleFilename')
        self.assertEqual(value.get_value(), 2)

    def test_03_ScanRuleType_ScanRuleFileGroup(self):
        """
        Test ScanRuleType with ScanRuleFileGroup
        """
        value = pykerio.enums.ScanRuleType(name='ScanRuleFileGroup')
        self.assertEqual(value.dump(), 'ScanRuleFileGroup')
        self.assertEqual(value.get_name(), 'ScanRuleFileGroup')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_ScanRuleType_FAIL(self):
        """
        Test ScanRuleType with FAIL
        """
        value = pykerio.enums.ScanRuleType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
