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

import pykerio.enums


class TestCase_CompareOperator(unittest.TestCase):
    def test_01_CompareOperator_Eq(self):
        """
        Test CompareOperator with Eq
        """
        compare_operator = pykerio.enums.CompareOperator(value='Eq')
        self.assertEquals(compare_operator.value, 'Eq')
        self.assertEquals(compare_operator.dump(), 'Eq')

    def test_02_CompareOperator_NotEq(self):
        """
        Test CompareOperator with NotEq
        """
        compare_operator = pykerio.enums.CompareOperator(value='NotEq')
        self.assertEquals(compare_operator.value, 'NotEq')
        self.assertEquals(compare_operator.dump(), 'NotEq')

    def test_03_CompareOperator_LessThan(self):
        """
        Test CompareOperator with LessThan
        """
        compare_operator = pykerio.enums.CompareOperator(value='LessThan')
        self.assertEquals(compare_operator.value, 'LessThan')
        self.assertEquals(compare_operator.dump(), 'LessThan')

    def test_04_CompareOperator_GreaterThan(self):
        """
        Test CompareOperator with GreaterThan
        """
        compare_operator = pykerio.enums.CompareOperator(value='GreaterThan')
        self.assertEquals(compare_operator.value, 'GreaterThan')
        self.assertEquals(compare_operator.dump(), 'GreaterThan')

    def test_05_CompareOperator_LessEq(self):
        """
        Test CompareOperator with LessEq
        """
        compare_operator = pykerio.enums.CompareOperator(value='LessEq')
        self.assertEquals(compare_operator.value, 'LessEq')
        self.assertEquals(compare_operator.dump(), 'LessEq')

    def test_06_CompareOperator_GreaterEq(self):
        """
        Test CompareOperator with GreaterEq
        """
        compare_operator = pykerio.enums.CompareOperator(value='GreaterEq')
        self.assertEquals(compare_operator.value, 'GreaterEq')
        self.assertEquals(compare_operator.dump(), 'GreaterEq')

    def test_07_CompareOperator_Like(self):
        """
        Test CompareOperator with Like
        """
        compare_operator = pykerio.enums.CompareOperator(value='Like')
        self.assertEquals(compare_operator.value, 'Like')
        self.assertEquals(compare_operator.dump(), 'Like')

    @unittest.expectedFailure
    def test_99_CompareOperator_FAIL(self):
        """
        Test CompareOperator with FAIL
        """
        compare_operator = pykerio.enums.CompareOperator(value='FAIL')
        self.assertEquals(compare_operator.value, 'FAIL')
        self.assertEquals(compare_operator.dump(), 'FAIL')
