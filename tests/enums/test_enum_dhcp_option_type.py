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

from pykerio.enums import DhcpOptionType


class TestCase_DhcpOptionType(unittest.TestCase):
    def test_00_DhcpBool(self):
        """
        Test DhcpOptionType with DhcpBool
        """
        value = DhcpOptionType.DhcpBool
        self.assertEqual(value.dump(), 'DhcpBool')
        self.assertEqual(value.name, 'DhcpBool')
        self.assertEqual(value.value, 0)

    def test_01_DhcpInt8(self):
        """
        Test DhcpOptionType with DhcpInt8
        """
        value = DhcpOptionType.DhcpInt8
        self.assertEqual(value.dump(), 'DhcpInt8')
        self.assertEqual(value.name, 'DhcpInt8')
        self.assertEqual(value.value, 1)

    def test_02_DhcpInt16(self):
        """
        Test DhcpOptionType with DhcpInt16
        """
        value = DhcpOptionType.DhcpInt16
        self.assertEqual(value.dump(), 'DhcpInt16')
        self.assertEqual(value.name, 'DhcpInt16')
        self.assertEqual(value.value, 2)

    def test_03_DhcpInt32(self):
        """
        Test DhcpOptionType with DhcpInt32
        """
        value = DhcpOptionType.DhcpInt32
        self.assertEqual(value.dump(), 'DhcpInt32')
        self.assertEqual(value.name, 'DhcpInt32')
        self.assertEqual(value.value, 3)

    def test_04_DhcpIpAddr(self):
        """
        Test DhcpOptionType with DhcpIpAddr
        """
        value = DhcpOptionType.DhcpIpAddr
        self.assertEqual(value.dump(), 'DhcpIpAddr')
        self.assertEqual(value.name, 'DhcpIpAddr')
        self.assertEqual(value.value, 4)

    def test_05_DhcpString(self):
        """
        Test DhcpOptionType with DhcpString
        """
        value = DhcpOptionType.DhcpString
        self.assertEqual(value.dump(), 'DhcpString')
        self.assertEqual(value.name, 'DhcpString')
        self.assertEqual(value.value, 5)

    def test_06_DhcpHex(self):
        """
        Test DhcpOptionType with DhcpHex
        """
        value = DhcpOptionType.DhcpHex
        self.assertEqual(value.dump(), 'DhcpHex')
        self.assertEqual(value.name, 'DhcpHex')
        self.assertEqual(value.value, 6)

    def test_07_DhcpTimeSigned(self):
        """
        Test DhcpOptionType with DhcpTimeSigned
        """
        value = DhcpOptionType.DhcpTimeSigned
        self.assertEqual(value.dump(), 'DhcpTimeSigned')
        self.assertEqual(value.name, 'DhcpTimeSigned')
        self.assertEqual(value.value, 7)

    def test_08_DhcpTimeUnsigned(self):
        """
        Test DhcpOptionType with DhcpTimeUnsigned
        """
        value = DhcpOptionType.DhcpTimeUnsigned
        self.assertEqual(value.dump(), 'DhcpTimeUnsigned')
        self.assertEqual(value.name, 'DhcpTimeUnsigned')
        self.assertEqual(value.value, 8)

    def test_09_DhcpInt8List(self):
        """
        Test DhcpOptionType with DhcpInt8List
        """
        value = DhcpOptionType.DhcpInt8List
        self.assertEqual(value.dump(), 'DhcpInt8List')
        self.assertEqual(value.name, 'DhcpInt8List')
        self.assertEqual(value.value, 9)

    def test_10_DhcpInt16List(self):
        """
        Test DhcpOptionType with DhcpInt16List
        """
        value = DhcpOptionType.DhcpInt16List
        self.assertEqual(value.dump(), 'DhcpInt16List')
        self.assertEqual(value.name, 'DhcpInt16List')
        self.assertEqual(value.value, 10)

    def test_11_DhcpInt32List(self):
        """
        Test DhcpOptionType with DhcpInt32List
        """
        value = DhcpOptionType.DhcpInt32List
        self.assertEqual(value.dump(), 'DhcpInt32List')
        self.assertEqual(value.name, 'DhcpInt32List')
        self.assertEqual(value.value, 11)

    def test_12_DhcpIpAddrList(self):
        """
        Test DhcpOptionType with DhcpIpAddrList
        """
        value = DhcpOptionType.DhcpIpAddrList
        self.assertEqual(value.dump(), 'DhcpIpAddrList')
        self.assertEqual(value.name, 'DhcpIpAddrList')
        self.assertEqual(value.value, 12)

    def test_13_DhcpIpPairList(self):
        """
        Test DhcpOptionType with DhcpIpPairList
        """
        value = DhcpOptionType.DhcpIpPairList
        self.assertEqual(value.dump(), 'DhcpIpPairList')
        self.assertEqual(value.name, 'DhcpIpPairList')
        self.assertEqual(value.value, 13)

    def test_14_DhcpIpMaskList(self):
        """
        Test DhcpOptionType with DhcpIpMaskList
        """
        value = DhcpOptionType.DhcpIpMaskList
        self.assertEqual(value.dump(), 'DhcpIpMaskList')
        self.assertEqual(value.name, 'DhcpIpMaskList')
        self.assertEqual(value.value, 14)

    def test_15_DhcpIpMaskIpList(self):
        """
        Test DhcpOptionType with DhcpIpMaskIpList
        """
        value = DhcpOptionType.DhcpIpMaskIpList
        self.assertEqual(value.dump(), 'DhcpIpMaskIpList')
        self.assertEqual(value.name, 'DhcpIpMaskIpList')
        self.assertEqual(value.value, 15)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test DhcpOptionType with FAIL
        """
        value = DhcpOptionType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
