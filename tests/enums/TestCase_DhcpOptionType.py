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


class TestCase_DhcpOptionType(unittest.TestCase):
    def test_00_DhcpOptionType_DhcpBool(self):
        """
        Test DhcpOptionType with DhcpBool
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpBool')
        self.assertEquals(value.dump(), 'DhcpBool')
        self.assertEquals(value.get_name(), 'DhcpBool')
        self.assertEquals(value.get_value(), 0)

    def test_01_DhcpOptionType_DhcpInt8(self):
        """
        Test DhcpOptionType with DhcpInt8
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpInt8')
        self.assertEquals(value.dump(), 'DhcpInt8')
        self.assertEquals(value.get_name(), 'DhcpInt8')
        self.assertEquals(value.get_value(), 1)

    def test_02_DhcpOptionType_DhcpInt16(self):
        """
        Test DhcpOptionType with DhcpInt16
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpInt16')
        self.assertEquals(value.dump(), 'DhcpInt16')
        self.assertEquals(value.get_name(), 'DhcpInt16')
        self.assertEquals(value.get_value(), 2)

    def test_03_DhcpOptionType_DhcpInt32(self):
        """
        Test DhcpOptionType with DhcpInt32
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpInt32')
        self.assertEquals(value.dump(), 'DhcpInt32')
        self.assertEquals(value.get_name(), 'DhcpInt32')
        self.assertEquals(value.get_value(), 3)

    def test_04_DhcpOptionType_DhcpIpAddr(self):
        """
        Test DhcpOptionType with DhcpIpAddr
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpIpAddr')
        self.assertEquals(value.dump(), 'DhcpIpAddr')
        self.assertEquals(value.get_name(), 'DhcpIpAddr')
        self.assertEquals(value.get_value(), 4)

    def test_05_DhcpOptionType_DhcpString(self):
        """
        Test DhcpOptionType with DhcpString
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpString')
        self.assertEquals(value.dump(), 'DhcpString')
        self.assertEquals(value.get_name(), 'DhcpString')
        self.assertEquals(value.get_value(), 5)

    def test_06_DhcpOptionType_DhcpHex(self):
        """
        Test DhcpOptionType with DhcpHex
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpHex')
        self.assertEquals(value.dump(), 'DhcpHex')
        self.assertEquals(value.get_name(), 'DhcpHex')
        self.assertEquals(value.get_value(), 6)

    def test_07_DhcpOptionType_DhcpTimeSigned(self):
        """
        Test DhcpOptionType with DhcpTimeSigned
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpTimeSigned')
        self.assertEquals(value.dump(), 'DhcpTimeSigned')
        self.assertEquals(value.get_name(), 'DhcpTimeSigned')
        self.assertEquals(value.get_value(), 7)

    def test_08_DhcpOptionType_DhcpTimeUnsigned(self):
        """
        Test DhcpOptionType with DhcpTimeUnsigned
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpTimeUnsigned')
        self.assertEquals(value.dump(), 'DhcpTimeUnsigned')
        self.assertEquals(value.get_name(), 'DhcpTimeUnsigned')
        self.assertEquals(value.get_value(), 8)

    def test_09_DhcpOptionType_DhcpInt8List(self):
        """
        Test DhcpOptionType with DhcpInt8List
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpInt8List')
        self.assertEquals(value.dump(), 'DhcpInt8List')
        self.assertEquals(value.get_name(), 'DhcpInt8List')
        self.assertEquals(value.get_value(), 9)

    def test_10_DhcpOptionType_DhcpInt16List(self):
        """
        Test DhcpOptionType with DhcpInt16List
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpInt16List')
        self.assertEquals(value.dump(), 'DhcpInt16List')
        self.assertEquals(value.get_name(), 'DhcpInt16List')
        self.assertEquals(value.get_value(), 10)

    def test_11_DhcpOptionType_DhcpInt32List(self):
        """
        Test DhcpOptionType with DhcpInt32List
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpInt32List')
        self.assertEquals(value.dump(), 'DhcpInt32List')
        self.assertEquals(value.get_name(), 'DhcpInt32List')
        self.assertEquals(value.get_value(), 11)

    def test_12_DhcpOptionType_DhcpIpAddrList(self):
        """
        Test DhcpOptionType with DhcpIpAddrList
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpIpAddrList')
        self.assertEquals(value.dump(), 'DhcpIpAddrList')
        self.assertEquals(value.get_name(), 'DhcpIpAddrList')
        self.assertEquals(value.get_value(), 12)

    def test_13_DhcpOptionType_DhcpIpPairList(self):
        """
        Test DhcpOptionType with DhcpIpPairList
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpIpPairList')
        self.assertEquals(value.dump(), 'DhcpIpPairList')
        self.assertEquals(value.get_name(), 'DhcpIpPairList')
        self.assertEquals(value.get_value(), 13)

    def test_14_DhcpOptionType_DhcpIpMaskList(self):
        """
        Test DhcpOptionType with DhcpIpMaskList
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpIpMaskList')
        self.assertEquals(value.dump(), 'DhcpIpMaskList')
        self.assertEquals(value.get_name(), 'DhcpIpMaskList')
        self.assertEquals(value.get_value(), 14)

    def test_15_DhcpOptionType_DhcpIpMaskIpList(self):
        """
        Test DhcpOptionType with DhcpIpMaskIpList
        """
        value = pykerio.enums.DhcpOptionType(name='DhcpIpMaskIpList')
        self.assertEquals(value.dump(), 'DhcpIpMaskIpList')
        self.assertEquals(value.get_name(), 'DhcpIpMaskIpList')
        self.assertEquals(value.get_value(), 15)

    @unittest.expectedFailure
    def test_99_DhcpOptionType_FAIL(self):
        """
        Test DhcpOptionType with FAIL
        """
        value = pykerio.enums.DhcpOptionType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
