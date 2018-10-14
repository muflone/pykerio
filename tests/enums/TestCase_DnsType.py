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


class TestCase_DnsType(unittest.TestCase):
    def test_00_DnsType_DnsTypeAny(self):
        """
        Test DnsType with DnsTypeAny
        """
        value = pykerio.enums.DnsType(name='DnsTypeAny')
        self.assertEquals(value.dump(), 'DnsTypeAny')
        self.assertEquals(value.get_name(), 'DnsTypeAny')
        self.assertEquals(value.get_value(), 0)

    def test_01_DnsType_DnsTypeA(self):
        """
        Test DnsType with DnsTypeA
        """
        value = pykerio.enums.DnsType(name='DnsTypeA')
        self.assertEquals(value.dump(), 'DnsTypeA')
        self.assertEquals(value.get_name(), 'DnsTypeA')
        self.assertEquals(value.get_value(), 1)

    def test_02_DnsType_DnsTypeAAAA(self):
        """
        Test DnsType with DnsTypeAAAA
        """
        value = pykerio.enums.DnsType(name='DnsTypeAAAA')
        self.assertEquals(value.dump(), 'DnsTypeAAAA')
        self.assertEquals(value.get_name(), 'DnsTypeAAAA')
        self.assertEquals(value.get_value(), 2)

    def test_03_DnsType_DnsTypeCname(self):
        """
        Test DnsType with DnsTypeCname
        """
        value = pykerio.enums.DnsType(name='DnsTypeCname')
        self.assertEquals(value.dump(), 'DnsTypeCname')
        self.assertEquals(value.get_name(), 'DnsTypeCname')
        self.assertEquals(value.get_value(), 3)

    def test_04_DnsType_DnsTypeMx(self):
        """
        Test DnsType with DnsTypeWhois
        """
        value = pykerio.enums.DnsType(name='DnsTypeMx')
        self.assertEquals(value.dump(), 'DnsTypeMx')
        self.assertEquals(value.get_name(), 'DnsTypeMx')
        self.assertEquals(value.get_value(), 4)

    def test_05_DnsType_DnsTypeNs(self):
        """
        Test DnsType with DnsTypeNs
        """
        value = pykerio.enums.DnsType(name='DnsTypeNs')
        self.assertEquals(value.dump(), 'DnsTypeNs')
        self.assertEquals(value.get_name(), 'DnsTypeNs')
        self.assertEquals(value.get_value(), 5)

    def test_06_DnsType_DnsTypePtr(self):
        """
        Test DnsType with DnsTypeWhois
        """
        value = pykerio.enums.DnsType(name='DnsTypePtr')
        self.assertEquals(value.dump(), 'DnsTypePtr')
        self.assertEquals(value.get_name(), 'DnsTypePtr')
        self.assertEquals(value.get_value(), 6)

    def test_07_DnsType_DnsTypeSoa(self):
        """
        Test DnsType with DnsTypeSoa
        """
        value = pykerio.enums.DnsType(name='DnsTypeSoa')
        self.assertEquals(value.dump(), 'DnsTypeSoa')
        self.assertEquals(value.get_name(), 'DnsTypeSoa')
        self.assertEquals(value.get_value(), 7)

    def test_08_DnsType_DnsTypeSpf(self):
        """
        Test DnsType with DnsTypeSpf
        """
        value = pykerio.enums.DnsType(name='DnsTypeSpf')
        self.assertEquals(value.dump(), 'DnsTypeSpf')
        self.assertEquals(value.get_name(), 'DnsTypeSpf')
        self.assertEquals(value.get_value(), 8)

    def test_09_DnsType_DnsTypeSrv(self):
        """
        Test DnsType with DnsTypeSrv
        """
        value = pykerio.enums.DnsType(name='DnsTypeSrv')
        self.assertEquals(value.dump(), 'DnsTypeSrv')
        self.assertEquals(value.get_name(), 'DnsTypeSrv')
        self.assertEquals(value.get_value(), 9)

    def test_10_DnsType_DnsTypeTxt(self):
        """
        Test DnsType with DnsTypeTxt
        """
        value = pykerio.enums.DnsType(name='DnsTypeTxt')
        self.assertEquals(value.dump(), 'DnsTypeTxt')
        self.assertEquals(value.get_name(), 'DnsTypeTxt')
        self.assertEquals(value.get_value(), 10)

    @unittest.expectedFailure
    def test_99_DnsType_FAIL(self):
        """
        Test DnsType with FAIL
        """
        value = pykerio.enums.DnsType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
