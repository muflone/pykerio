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

from pykerio.enums import CompareOperator


class TestCase_CompareOperator(unittest.TestCase):
    def test_00_Eq(self):
        """
        Test CompareOperator with Eq
        """
        value = CompareOperator.Eq
        self.assertEqual(value.dump(), 'Eq')
        self.assertEqual(value.name, 'Eq')
        self.assertEqual(value.value, 0)

    def test_01_NotEq(self):
        """
        Test CompareOperator with NotEq
        """
        value = CompareOperator.NotEq
        self.assertEqual(value.dump(), 'NotEq')
        self.assertEqual(value.name, 'NotEq')
        self.assertEqual(value.value, 1)

    def test_02_LessThan(self):
        """
        Test CompareOperator with LessThan
        """
        value = CompareOperator.LessThan
        self.assertEqual(value.dump(), 'LessThan')
        self.assertEqual(value.name, 'LessThan')
        self.assertEqual(value.value, 2)

    def test_03_GreaterThan(self):
        """
        Test CompareOperator with GreaterThan
        """
        value = CompareOperator.GreaterThan
        self.assertEqual(value.dump(), 'GreaterThan')
        self.assertEqual(value.name, 'GreaterThan')
        self.assertEqual(value.value, 3)

    def test_04_LessEq(self):
        """
        Test CompareOperator with LessEq
        """
        value = CompareOperator.LessEq
        self.assertEqual(value.dump(), 'LessEq')
        self.assertEqual(value.name, 'LessEq')
        self.assertEqual(value.value, 4)

    def test_05_GreaterEq(self):
        """
        Test CompareOperator with GreaterEq
        """
        value = CompareOperator.GreaterEq
        self.assertEqual(value.dump(), 'GreaterEq')
        self.assertEqual(value.name, 'GreaterEq')
        self.assertEqual(value.value, 5)

    def test_06_Like(self):
        """
        Test CompareOperator with Like
        """
        value = CompareOperator.Like
        self.assertEqual(value.dump(), 'Like')
        self.assertEqual(value.name, 'Like')
        self.assertEqual(value.value, 6)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test CompareOperator with FAIL
        """
        value = CompareOperator.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
