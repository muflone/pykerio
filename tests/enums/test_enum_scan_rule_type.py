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

from pykerio.enums import ScanRuleType


class TestCase_ScanRuleType(unittest.TestCase):
    def test_00_ScanRuleUrl(self):
        """
        Test ScanRuleType with ScanRuleUrl
        """
        value = ScanRuleType.ScanRuleUrl
        self.assertEqual(value.dump(), 'ScanRuleUrl')
        self.assertEqual(value.name, 'ScanRuleUrl')
        self.assertEqual(value.value, 0)

    def test_01_ScanRuleMime(self):
        """
        Test ScanRuleType with ScanRuleMime
        """
        value = ScanRuleType.ScanRuleMime
        self.assertEqual(value.dump(), 'ScanRuleMime')
        self.assertEqual(value.name, 'ScanRuleMime')
        self.assertEqual(value.value, 1)

    def test_02_ScanRuleFilename(self):
        """
        Test ScanRuleType with ScanRuleFilename
        """
        value = ScanRuleType.ScanRuleFilename
        self.assertEqual(value.dump(), 'ScanRuleFilename')
        self.assertEqual(value.name, 'ScanRuleFilename')
        self.assertEqual(value.value, 2)

    def test_03_ScanRuleFileGroup(self):
        """
        Test ScanRuleType with ScanRuleFileGroup
        """
        value = ScanRuleType.ScanRuleFileGroup
        self.assertEqual(value.dump(), 'ScanRuleFileGroup')
        self.assertEqual(value.name, 'ScanRuleFileGroup')
        self.assertEqual(value.value, 3)
