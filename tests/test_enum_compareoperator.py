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
        value = pykerio.enums.CompareOperator(value='Eq')
        self.assertEquals(value.value, 'Eq')
        self.assertEquals(value.dump(), 'Eq')

    def test_02_CompareOperator_NotEq(self):
        """
        Test CompareOperator with NotEq
        """
        value = pykerio.enums.CompareOperator(value='NotEq')
        self.assertEquals(value.value, 'NotEq')
        self.assertEquals(value.dump(), 'NotEq')

    def test_03_CompareOperator_LessThan(self):
        """
        Test CompareOperator with LessThan
        """
        value = pykerio.enums.CompareOperator(value='LessThan')
        self.assertEquals(value.value, 'LessThan')
        self.assertEquals(value.dump(), 'LessThan')

    def test_04_CompareOperator_GreaterThan(self):
        """
        Test CompareOperator with GreaterThan
        """
        value = pykerio.enums.CompareOperator(value='GreaterThan')
        self.assertEquals(value.value, 'GreaterThan')
        self.assertEquals(value.dump(), 'GreaterThan')

    def test_05_CompareOperator_LessEq(self):
        """
        Test CompareOperator with LessEq
        """
        value = pykerio.enums.CompareOperator(value='LessEq')
        self.assertEquals(value.value, 'LessEq')
        self.assertEquals(value.dump(), 'LessEq')

    def test_06_CompareOperator_GreaterEq(self):
        """
        Test CompareOperator with GreaterEq
        """
        value = pykerio.enums.CompareOperator(value='GreaterEq')
        self.assertEquals(value.value, 'GreaterEq')
        self.assertEquals(value.dump(), 'GreaterEq')

    def test_07_CompareOperator_Like(self):
        """
        Test CompareOperator with Like
        """
        value = pykerio.enums.CompareOperator(value='Like')
        self.assertEquals(value.value, 'Like')
        self.assertEquals(value.dump(), 'Like')

    @unittest.expectedFailure
    def test_99_CompareOperator_FAIL(self):
        """
        Test CompareOperator with FAIL
        """
        value = pykerio.enums.CompareOperator(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
