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


class TestCase_UpdateStatus(unittest.TestCase):
    def test_00_UpdateStatus_UpdateStatusOk(self):
        """
        Test UpdateStatus with UpdateStatusOk
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusOk')
        self.assertEqual(value.dump(), 'UpdateStatusOk')
        self.assertEqual(value.get_name(), 'UpdateStatusOk')
        self.assertEqual(value.get_value(), 0)

    def test_01_UpdateStatus_UpdateStatusChecking(self):
        """
        Test UpdateStatus with UpdateStatusChecking
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusChecking')
        self.assertEqual(value.dump(), 'UpdateStatusChecking')
        self.assertEqual(value.get_name(), 'UpdateStatusChecking')
        self.assertEqual(value.get_value(), 1)

    def test_02_UpdateStatus_UpdateStatusCheckFailed(self):
        """
        Test UpdateStatus with UpdateStatusCheckFailed
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusCheckFailed')
        self.assertEqual(value.dump(), 'UpdateStatusCheckFailed')
        self.assertEqual(value.get_name(), 'UpdateStatusCheckFailed')
        self.assertEqual(value.get_value(), 2)

    def test_03_UpdateStatus_UpdateStatusDownloadOk(self):
        """
        Test UpdateStatus with UpdateStatusDownloadOk
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusDownloadOk')
        self.assertEqual(value.dump(), 'UpdateStatusDownloadOk')
        self.assertEqual(value.get_name(), 'UpdateStatusDownloadOk')
        self.assertEqual(value.get_value(), 3)

    def test_04_UpdateStatus_UpdateStatusDownloading(self):
        """
        Test UpdateStatus with UpdateStatusDownloading
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusDownloading')
        self.assertEqual(value.dump(), 'UpdateStatusDownloading')
        self.assertEqual(value.get_name(), 'UpdateStatusDownloading')
        self.assertEqual(value.get_value(), 4)

    def test_05_UpdateStatus_UpdateStatusDownloadFailed(self):
        """
        Test UpdateStatus with UpdateStatusDownloadFailed
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusDownloadFailed')
        self.assertEqual(value.dump(), 'UpdateStatusDownloadFailed')
        self.assertEqual(value.get_name(), 'UpdateStatusDownloadFailed')
        self.assertEqual(value.get_value(), 5)

    def test_06_UpdateStatus_UpdateStatusUpgrading(self):
        """
        Test UpdateStatus with UpdateStatusUpgrading
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusUpgrading')
        self.assertEqual(value.dump(), 'UpdateStatusUpgrading')
        self.assertEqual(value.get_name(), 'UpdateStatusUpgrading')
        self.assertEqual(value.get_value(), 6)

    def test_07_UpdateStatus_UpdateStatusUpgradeFailed(self):
        """
        Test UpdateStatus with UpdateStatusUpgradeFailed
        """
        value = pykerio.enums.UpdateStatus(name='UpdateStatusUpgradeFailed')
        self.assertEqual(value.dump(), 'UpdateStatusUpgradeFailed')
        self.assertEqual(value.get_name(), 'UpdateStatusUpgradeFailed')
        self.assertEqual(value.get_value(), 7)

    @unittest.expectedFailure
    def test_99_UpdateStatus_FAIL(self):
        """
        Test UpdateStatus with FAIL
        """
        value = pykerio.enums.UpdateStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
