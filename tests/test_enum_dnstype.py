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


class TestCase_DnsType(unittest.TestCase):
    def test_01_DnsType_DnsTypeAny(self):
        """
        Test DnsType with DnsTypeAny
        """
        value = pykerio.enums.DnsType(value='DnsTypeAny')
        self.assertEquals(value.value, 'DnsTypeAny')
        self.assertEquals(value.dump(), 'DnsTypeAny')

    def test_02_DnsType_DnsTypeA(self):
        """
        Test DnsType with DnsTypeA
        """
        value = pykerio.enums.DnsType(value='DnsTypeA')
        self.assertEquals(value.value, 'DnsTypeA')
        self.assertEquals(value.dump(), 'DnsTypeA')

    def test_03_DnsType_DnsTypeAAAA(self):
        """
        Test DnsType with DnsTypeAAAA
        """
        value = pykerio.enums.DnsType(value='DnsTypeAAAA')
        self.assertEquals(value.value, 'DnsTypeAAAA')
        self.assertEquals(value.dump(), 'DnsTypeAAAA')

    def test_04_DnsType_DnsTypeCname(self):
        """
        Test DnsType with DnsTypeCname
        """
        value = pykerio.enums.DnsType(value='DnsTypeCname')
        self.assertEquals(value.value, 'DnsTypeCname')
        self.assertEquals(value.dump(), 'DnsTypeCname')

    def test_05_DnsType_DnsTypeMx(self):
        """
        Test DnsType with DnsTypeWhois
        """
        value = pykerio.enums.DnsType(value='DnsTypeMx')
        self.assertEquals(value.value, 'DnsTypeMx')
        self.assertEquals(value.dump(), 'DnsTypeMx')

    def test_06_DnsType_DnsTypeNs(self):
        """
        Test DnsType with DnsTypeNs
        """
        value = pykerio.enums.DnsType(value='DnsTypeNs')
        self.assertEquals(value.value, 'DnsTypeNs')
        self.assertEquals(value.dump(), 'DnsTypeNs')

    def test_07_DnsType_DnsTypePtr(self):
        """
        Test DnsType with DnsTypeWhois
        """
        value = pykerio.enums.DnsType(value='DnsTypePtr')
        self.assertEquals(value.value, 'DnsTypePtr')
        self.assertEquals(value.dump(), 'DnsTypePtr')

    def test_08_DnsType_DnsTypeSoa(self):
        """
        Test DnsType with DnsTypeSoa
        """
        value = pykerio.enums.DnsType(value='DnsTypeSoa')
        self.assertEquals(value.value, 'DnsTypeSoa')
        self.assertEquals(value.dump(), 'DnsTypeSoa')

    def test_09_DnsType_DnsTypeSpf(self):
        """
        Test DnsType with DnsTypeSpf
        """
        value = pykerio.enums.DnsType(value='DnsTypeSpf')
        self.assertEquals(value.value, 'DnsTypeSpf')
        self.assertEquals(value.dump(), 'DnsTypeSpf')

    def test_10_DnsType_DnsTypeTxt(self):
        """
        Test DnsType with DnsTypeTxt
        """
        value = pykerio.enums.DnsType(value='DnsTypeTxt')
        self.assertEquals(value.value, 'DnsTypeTxt')
        self.assertEquals(value.dump(), 'DnsTypeTxt')

    def test_10_DnsType_DnsTypeSrv(self):
        """
        Test DnsType with DnsTypeSrv
        """
        value = pykerio.enums.DnsType(value='DnsTypeSrv')
        self.assertEquals(value.value, 'DnsTypeSrv')
        self.assertEquals(value.dump(), 'DnsTypeSrv')

    @unittest.expectedFailure
    def test_99_DnsType_FAIL(self):
        """
        Test DnsType with FAIL
        """
        value = pykerio.enums.DnsType(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
