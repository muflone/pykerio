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


class TestCase_AntivirusStatus(unittest.TestCase):
    def test_00_AntivirusStatus_AntivirusOk(self):
        """
        Test AntivirusStatus with AntivirusOk
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusOk')
        self.assertEquals(value.dump(), 'AntivirusOk')
        self.assertEquals(value.get_name(), 'AntivirusOk')
        self.assertEquals(value.get_value(), 0)

    def test_01_AntivirusStatus_AntivirusNotActive(self):
        """
        Test AntivirusStatus with AntivirusNotActive
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusNotActive')
        self.assertEquals(value.dump(), 'AntivirusNotActive')
        self.assertEquals(value.get_name(), 'AntivirusNotActive')
        self.assertEquals(value.get_value(), 1)

    def test_02_AntivirusStatus_AntivirusInternalFailed(self):
        """
        Test AntivirusStatus with AntivirusInternalFailed
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusInternalFailed')
        self.assertEquals(value.dump(), 'AntivirusInternalFailed')
        self.assertEquals(value.get_name(), 'AntivirusInternalFailed')
        self.assertEquals(value.get_value(), 2)

    def test_03_AntivirusStatus_AntivirusExternalFailed(self):
        """
        Test AntivirusStatus with AntivirusExternalFailed
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusExternalFailed')
        self.assertEquals(value.dump(), 'AntivirusExternalFailed')
        self.assertEquals(value.get_name(), 'AntivirusExternalFailed')
        self.assertEquals(value.get_value(), 3)

    def test_04_AntivirusStatus_AntivirusBothFailed(self):
        """
        Test AntivirusStatus with AntivirusBothFailed
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusBothFailed')
        self.assertEquals(value.dump(), 'AntivirusBothFailed')
        self.assertEquals(value.get_name(), 'AntivirusBothFailed')
        self.assertEquals(value.get_value(), 4)

    def test_05_AntivirusStatus_AntivirusWaitingForInitialDb(self):
        """
        Test AntivirusStatus with AntivirusWaitingForInitialDb
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusWaitingForInitialDb')
        self.assertEquals(value.dump(), 'AntivirusWaitingForInitialDb')
        self.assertEquals(value.get_name(), 'AntivirusWaitingForInitialDb')
        self.assertEquals(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_AntivirusStatus_FAIL(self):
        """
        Test AntivirusStatus with FAIL
        """
        value = pykerio.enums.AntivirusStatus(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
