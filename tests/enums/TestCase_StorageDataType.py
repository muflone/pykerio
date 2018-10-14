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


class TestCase_StorageDataType(unittest.TestCase):
    def test_00_StorageDataType_StorageDataStar(self):
        """
        Test StorageDataType with StorageDataStar
        """
        value = pykerio.enums.StorageDataType(name='StorageDataStar')
        self.assertEquals(value.dump(), 'StorageDataStar')
        self.assertEquals(value.get_name(), 'StorageDataStar')
        self.assertEquals(value.get_value(), 0)

    def test_01_StorageDataType_StorageDataLogs(self):
        """
        Test StorageDataType with StorageDataLogs
        """
        value = pykerio.enums.StorageDataType(name='StorageDataLogs')
        self.assertEquals(value.dump(), 'StorageDataLogs')
        self.assertEquals(value.get_name(), 'StorageDataLogs')
        self.assertEquals(value.get_value(), 1)

    def test_02_StorageDataType_StorageDataCrash(self):
        """
        Test StorageDataType with StorageDataCrash
        """
        value = pykerio.enums.StorageDataType(name='StorageDataCrash')
        self.assertEquals(value.dump(), 'StorageDataCrash')
        self.assertEquals(value.get_name(), 'StorageDataCrash')
        self.assertEquals(value.get_value(), 2)

    def test_03_StorageDataType_StorageDataPktdump(self):
        """
        Test StorageDataType with StorageDataPktdump
        """
        value = pykerio.enums.StorageDataType(name='StorageDataPktdump')
        self.assertEquals(value.dump(), 'StorageDataPktdump')
        self.assertEquals(value.get_name(), 'StorageDataPktdump')
        self.assertEquals(value.get_value(), 3)

    def test_04_StorageDataType_StorageDataUpdate(self):
        """
        Test StorageDataType with StorageDataUpdate
        """
        value = pykerio.enums.StorageDataType(name='StorageDataUpdate')
        self.assertEquals(value.dump(), 'StorageDataUpdate')
        self.assertEquals(value.get_name(), 'StorageDataUpdate')
        self.assertEquals(value.get_value(), 4)

    def test_05_StorageDataType_StorageDataQuarantine(self):
        """
        Test StorageDataType with StorageDataQuarantine
        """
        value = pykerio.enums.StorageDataType(name='StorageDataQuarantine')
        self.assertEquals(value.dump(), 'StorageDataQuarantine')
        self.assertEquals(value.get_name(), 'StorageDataQuarantine')
        self.assertEquals(value.get_value(), 5)

    def test_06_StorageDataType_StorageDataHttpCache(self):
        """
        Test StorageDataType with StorageDataHttpCache
        """
        value = pykerio.enums.StorageDataType(name='StorageDataHttpCache')
        self.assertEquals(value.dump(), 'StorageDataHttpCache')
        self.assertEquals(value.get_name(), 'StorageDataHttpCache')
        self.assertEquals(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_StorageDataType_FAIL(self):
        """
        Test StorageDataType with FAIL
        """
        value = pykerio.enums.StorageDataType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
