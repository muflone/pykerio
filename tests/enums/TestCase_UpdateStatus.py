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


class TestCase_UpdateStatus(unittest.TestCase):
    def test_00_UpdateStatus_UpdateStatusOk(self):
        """
        Test UpdateStatus with UpdateStatusOk
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusOk')
        self.assertEquals(value.dump(), 'UpdateStatusOk')
        self.assertEquals(value.get_name(), 'UpdateStatusOk')
        self.assertEquals(value.get_value(), 0)

    def test_01_UpdateStatus_UpdateStatusChecking(self):
        """
        Test UpdateStatus with UpdateStatusChecking
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusChecking')
        self.assertEquals(value.dump(), 'UpdateStatusChecking')
        self.assertEquals(value.get_name(), 'UpdateStatusChecking')
        self.assertEquals(value.get_value(), 1)

    def test_02_UpdateStatus_UpdateStatusCheckFailed(self):
        """
        Test UpdateStatus with UpdateStatusCheckFailed
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusCheckFailed')
        self.assertEquals(value.dump(), 'UpdateStatusCheckFailed')
        self.assertEquals(value.get_name(), 'UpdateStatusCheckFailed')
        self.assertEquals(value.get_value(), 2)

    def test_03_UpdateStatus_UpdateStatusDownloadOk(self):
        """
        Test UpdateStatus with UpdateStatusDownloadOk
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusDownloadOk')
        self.assertEquals(value.dump(), 'UpdateStatusDownloadOk')
        self.assertEquals(value.get_name(), 'UpdateStatusDownloadOk')
        self.assertEquals(value.get_value(), 3)

    def test_04_UpdateStatus_UpdateStatusDownloading(self):
        """
        Test UpdateStatus with UpdateStatusDownloading
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusDownloading')
        self.assertEquals(value.dump(), 'UpdateStatusDownloading')
        self.assertEquals(value.get_name(), 'UpdateStatusDownloading')
        self.assertEquals(value.get_value(), 4)

    def test_05_UpdateStatus_UpdateStatusDownloadFailed(self):
        """
        Test UpdateStatus with UpdateStatusDownloadFailed
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusDownloadFailed')
        self.assertEquals(value.dump(), 'UpdateStatusDownloadFailed')
        self.assertEquals(value.get_name(), 'UpdateStatusDownloadFailed')
        self.assertEquals(value.get_value(), 5)

    def test_06_UpdateStatus_UpdateStatusUpgrading(self):
        """
        Test UpdateStatus with UpdateStatusUpgrading
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusUpgrading')
        self.assertEquals(value.dump(), 'UpdateStatusUpgrading')
        self.assertEquals(value.get_name(), 'UpdateStatusUpgrading')
        self.assertEquals(value.get_value(), 6)

    def test_07_UpdateStatus_UpdateStatusUpgradeFailed(self):
        """
        Test UpdateStatus with UpdateStatusUpgradeFailed
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusUpgradeFailed')
        self.assertEquals(value.dump(), 'UpdateStatusUpgradeFailed')
        self.assertEquals(value.get_name(), 'UpdateStatusUpgradeFailed')
        self.assertEquals(value.get_value(), 7)

    @unittest.expectedFailure
    def test_99_UpdateStatus_FAIL(self):
        """
        Test UpdateStatus with FAIL
        """
        value = pykerio.enums.UpdateStatus(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
