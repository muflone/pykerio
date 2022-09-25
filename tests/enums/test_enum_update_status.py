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

from pykerio.enums import UpdateStatus


class TestCase_UpdateStatus(unittest.TestCase):
    def test_00_UpdateStatusOk(self):
        """
        Test UpdateStatus with UpdateStatusOk
        """
        value = UpdateStatus.UpdateStatusOk
        self.assertEqual(value.dump(), 'UpdateStatusOk')
        self.assertEqual(value.name, 'UpdateStatusOk')
        self.assertEqual(value.value, 0)

    def test_01_UpdateStatusChecking(self):
        """
        Test UpdateStatus with UpdateStatusChecking
        """
        value = UpdateStatus.UpdateStatusChecking
        self.assertEqual(value.dump(), 'UpdateStatusChecking')
        self.assertEqual(value.name, 'UpdateStatusChecking')
        self.assertEqual(value.value, 1)

    def test_02_UpdateStatusCheckFailed(self):
        """
        Test UpdateStatus with UpdateStatusCheckFailed
        """
        value = UpdateStatus.UpdateStatusCheckFailed
        self.assertEqual(value.dump(), 'UpdateStatusCheckFailed')
        self.assertEqual(value.name, 'UpdateStatusCheckFailed')
        self.assertEqual(value.value, 2)

    def test_03_UpdateStatusDownloadOk(self):
        """
        Test UpdateStatus with UpdateStatusDownloadOk
        """
        value = UpdateStatus.UpdateStatusDownloadOk
        self.assertEqual(value.dump(), 'UpdateStatusDownloadOk')
        self.assertEqual(value.name, 'UpdateStatusDownloadOk')
        self.assertEqual(value.value, 3)

    def test_04_UpdateStatusDownloading(self):
        """
        Test UpdateStatus with UpdateStatusDownloading
        """
        value = UpdateStatus.UpdateStatusDownloading
        self.assertEqual(value.dump(), 'UpdateStatusDownloading')
        self.assertEqual(value.name, 'UpdateStatusDownloading')
        self.assertEqual(value.value, 4)

    def test_05_UpdateStatusDownloadFailed(self):
        """
        Test UpdateStatus with UpdateStatusDownloadFailed
        """
        value = UpdateStatus.UpdateStatusDownloadFailed
        self.assertEqual(value.dump(), 'UpdateStatusDownloadFailed')
        self.assertEqual(value.name, 'UpdateStatusDownloadFailed')
        self.assertEqual(value.value, 5)

    def test_06_UpdateStatusUpgrading(self):
        """
        Test UpdateStatus with UpdateStatusUpgrading
        """
        value = UpdateStatus.UpdateStatusUpgrading
        self.assertEqual(value.dump(), 'UpdateStatusUpgrading')
        self.assertEqual(value.name, 'UpdateStatusUpgrading')
        self.assertEqual(value.value, 6)

    def test_07_UpdateStatusUpgradeFailed(self):
        """
        Test UpdateStatus with UpdateStatusUpgradeFailed
        """
        value = UpdateStatus.UpdateStatusUpgradeFailed
        self.assertEqual(value.dump(), 'UpdateStatusUpgradeFailed')
        self.assertEqual(value.name, 'UpdateStatusUpgradeFailed')
        self.assertEqual(value.value, 7)
