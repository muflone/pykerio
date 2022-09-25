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


class TestCase_DnsType(unittest.TestCase):
    def test_00_DnsTypeAny(self):
        """
        Test DnsType with DnsTypeAny
        """
        value = pykerio.enums.DnsType(name='DnsTypeAny')
        self.assertEqual(value.dump(), 'DnsTypeAny')
        self.assertEqual(value.get_name(), 'DnsTypeAny')
        self.assertEqual(value.get_value(), 0)

    def test_01_DnsTypeA(self):
        """
        Test DnsType with DnsTypeA
        """
        value = pykerio.enums.DnsType(name='DnsTypeA')
        self.assertEqual(value.dump(), 'DnsTypeA')
        self.assertEqual(value.get_name(), 'DnsTypeA')
        self.assertEqual(value.get_value(), 1)

    def test_02_DnsTypeAAAA(self):
        """
        Test DnsType with DnsTypeAAAA
        """
        value = pykerio.enums.DnsType(name='DnsTypeAAAA')
        self.assertEqual(value.dump(), 'DnsTypeAAAA')
        self.assertEqual(value.get_name(), 'DnsTypeAAAA')
        self.assertEqual(value.get_value(), 2)

    def test_03_DnsTypeCname(self):
        """
        Test DnsType with DnsTypeCname
        """
        value = pykerio.enums.DnsType(name='DnsTypeCname')
        self.assertEqual(value.dump(), 'DnsTypeCname')
        self.assertEqual(value.get_name(), 'DnsTypeCname')
        self.assertEqual(value.get_value(), 3)

    def test_04_DnsTypeMx(self):
        """
        Test DnsType with DnsTypeWhois
        """
        value = pykerio.enums.DnsType(name='DnsTypeMx')
        self.assertEqual(value.dump(), 'DnsTypeMx')
        self.assertEqual(value.get_name(), 'DnsTypeMx')
        self.assertEqual(value.get_value(), 4)

    def test_05_DnsTypeNs(self):
        """
        Test DnsType with DnsTypeNs
        """
        value = pykerio.enums.DnsType(name='DnsTypeNs')
        self.assertEqual(value.dump(), 'DnsTypeNs')
        self.assertEqual(value.get_name(), 'DnsTypeNs')
        self.assertEqual(value.get_value(), 5)

    def test_06_DnsTypePtr(self):
        """
        Test DnsType with DnsTypeWhois
        """
        value = pykerio.enums.DnsType(name='DnsTypePtr')
        self.assertEqual(value.dump(), 'DnsTypePtr')
        self.assertEqual(value.get_name(), 'DnsTypePtr')
        self.assertEqual(value.get_value(), 6)

    def test_07_DnsTypeSoa(self):
        """
        Test DnsType with DnsTypeSoa
        """
        value = pykerio.enums.DnsType(name='DnsTypeSoa')
        self.assertEqual(value.dump(), 'DnsTypeSoa')
        self.assertEqual(value.get_name(), 'DnsTypeSoa')
        self.assertEqual(value.get_value(), 7)

    def test_08_DnsTypeSpf(self):
        """
        Test DnsType with DnsTypeSpf
        """
        value = pykerio.enums.DnsType(name='DnsTypeSpf')
        self.assertEqual(value.dump(), 'DnsTypeSpf')
        self.assertEqual(value.get_name(), 'DnsTypeSpf')
        self.assertEqual(value.get_value(), 8)

    def test_09_DnsTypeSrv(self):
        """
        Test DnsType with DnsTypeSrv
        """
        value = pykerio.enums.DnsType(name='DnsTypeSrv')
        self.assertEqual(value.dump(), 'DnsTypeSrv')
        self.assertEqual(value.get_name(), 'DnsTypeSrv')
        self.assertEqual(value.get_value(), 9)

    def test_10_DnsTypeTxt(self):
        """
        Test DnsType with DnsTypeTxt
        """
        value = pykerio.enums.DnsType(name='DnsTypeTxt')
        self.assertEqual(value.dump(), 'DnsTypeTxt')
        self.assertEqual(value.get_name(), 'DnsTypeTxt')
        self.assertEqual(value.get_value(), 10)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test DnsType with FAIL
        """
        value = pykerio.enums.DnsType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
