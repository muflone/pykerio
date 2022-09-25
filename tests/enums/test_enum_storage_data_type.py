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


class TestCase_StorageDataType(unittest.TestCase):
    def test_00_StorageDataStar(self):
        """
        Test StorageDataType with StorageDataStar
        """
        value = pykerio.enums.StorageDataType(name='StorageDataStar')
        self.assertEqual(value.dump(), 'StorageDataStar')
        self.assertEqual(value.get_name(), 'StorageDataStar')
        self.assertEqual(value.get_value(), 0)

    def test_01_StorageDataLogs(self):
        """
        Test StorageDataType with StorageDataLogs
        """
        value = pykerio.enums.StorageDataType(name='StorageDataLogs')
        self.assertEqual(value.dump(), 'StorageDataLogs')
        self.assertEqual(value.get_name(), 'StorageDataLogs')
        self.assertEqual(value.get_value(), 1)

    def test_02_StorageDataCrash(self):
        """
        Test StorageDataType with StorageDataCrash
        """
        value = pykerio.enums.StorageDataType(name='StorageDataCrash')
        self.assertEqual(value.dump(), 'StorageDataCrash')
        self.assertEqual(value.get_name(), 'StorageDataCrash')
        self.assertEqual(value.get_value(), 2)

    def test_03_StorageDataPktdump(self):
        """
        Test StorageDataType with StorageDataPktdump
        """
        value = pykerio.enums.StorageDataType(name='StorageDataPktdump')
        self.assertEqual(value.dump(), 'StorageDataPktdump')
        self.assertEqual(value.get_name(), 'StorageDataPktdump')
        self.assertEqual(value.get_value(), 3)

    def test_04_StorageDataUpdate(self):
        """
        Test StorageDataType with StorageDataUpdate
        """
        value = pykerio.enums.StorageDataType(name='StorageDataUpdate')
        self.assertEqual(value.dump(), 'StorageDataUpdate')
        self.assertEqual(value.get_name(), 'StorageDataUpdate')
        self.assertEqual(value.get_value(), 4)

    def test_05_StorageDataQuarantine(self):
        """
        Test StorageDataType with StorageDataQuarantine
        """
        value = pykerio.enums.StorageDataType(name='StorageDataQuarantine')
        self.assertEqual(value.dump(), 'StorageDataQuarantine')
        self.assertEqual(value.get_name(), 'StorageDataQuarantine')
        self.assertEqual(value.get_value(), 5)

    def test_06_StorageDataHttpCache(self):
        """
        Test StorageDataType with StorageDataHttpCache
        """
        value = pykerio.enums.StorageDataType(name='StorageDataHttpCache')
        self.assertEqual(value.dump(), 'StorageDataHttpCache')
        self.assertEqual(value.get_name(), 'StorageDataHttpCache')
        self.assertEqual(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test StorageDataType with FAIL
        """
        value = pykerio.enums.StorageDataType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
