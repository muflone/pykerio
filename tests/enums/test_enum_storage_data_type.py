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

from pykerio.enums import StorageDataType


class TestCase_StorageDataType(unittest.TestCase):
    def test_00_StorageDataStar(self):
        """
        Test StorageDataType with StorageDataStar
        """
        value = StorageDataType.StorageDataStar
        self.assertEqual(value.dump(), 'StorageDataStar')
        self.assertEqual(value.name, 'StorageDataStar')
        self.assertEqual(value.value, 0)

    def test_01_StorageDataLogs(self):
        """
        Test StorageDataType with StorageDataLogs
        """
        value = StorageDataType.StorageDataLogs
        self.assertEqual(value.dump(), 'StorageDataLogs')
        self.assertEqual(value.name, 'StorageDataLogs')
        self.assertEqual(value.value, 1)

    def test_02_StorageDataCrash(self):
        """
        Test StorageDataType with StorageDataCrash
        """
        value = StorageDataType.StorageDataCrash
        self.assertEqual(value.dump(), 'StorageDataCrash')
        self.assertEqual(value.name, 'StorageDataCrash')
        self.assertEqual(value.value, 2)

    def test_03_StorageDataPktdump(self):
        """
        Test StorageDataType with StorageDataPktdump
        """
        value = StorageDataType.StorageDataPktdump
        self.assertEqual(value.dump(), 'StorageDataPktdump')
        self.assertEqual(value.name, 'StorageDataPktdump')
        self.assertEqual(value.value, 3)

    def test_04_StorageDataUpdate(self):
        """
        Test StorageDataType with StorageDataUpdate
        """
        value = StorageDataType.StorageDataUpdate
        self.assertEqual(value.dump(), 'StorageDataUpdate')
        self.assertEqual(value.name, 'StorageDataUpdate')
        self.assertEqual(value.value, 4)

    def test_05_StorageDataQuarantine(self):
        """
        Test StorageDataType with StorageDataQuarantine
        """
        value = StorageDataType.StorageDataQuarantine
        self.assertEqual(value.dump(), 'StorageDataQuarantine')
        self.assertEqual(value.name, 'StorageDataQuarantine')
        self.assertEqual(value.value, 5)

    def test_06_StorageDataHttpCache(self):
        """
        Test StorageDataType with StorageDataHttpCache
        """
        value = StorageDataType.StorageDataHttpCache
        self.assertEqual(value.dump(), 'StorageDataHttpCache')
        self.assertEqual(value.name, 'StorageDataHttpCache')
        self.assertEqual(value.value, 6)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test StorageDataType with FAIL
        """
        value = StorageDataType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
