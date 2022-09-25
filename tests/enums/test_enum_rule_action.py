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

from pykerio.enums import RuleAction


class TestCase_RuleAction(unittest.TestCase):
    def test_00_Allow(self):
        """
        Test RuleAction with Allow
        """
        value = RuleAction.Allow
        self.assertEqual(value.dump(), 'Allow')
        self.assertEqual(value.name, 'Allow')
        self.assertEqual(value.value, 0)

    def test_01_Deny(self):
        """
        Test RuleAction with Deny
        """
        value = RuleAction.Deny
        self.assertEqual(value.dump(), 'Deny')
        self.assertEqual(value.name, 'Deny')
        self.assertEqual(value.value, 1)

    def test_02_Drop(self):
        """
        Test RuleAction with Drop
        """
        value = RuleAction.Drop
        self.assertEqual(value.dump(), 'Drop')
        self.assertEqual(value.name, 'Drop')
        self.assertEqual(value.value, 2)

    def test_03_NotSet(self):
        """
        Test RuleAction with NotSet
        """
        value = RuleAction.NotSet
        self.assertEqual(value.dump(), 'NotSet')
        self.assertEqual(value.name, 'NotSet')
        self.assertEqual(value.value, 3)
