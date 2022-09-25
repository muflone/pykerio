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


class TestCase_AntivirusUpdatePhases(unittest.TestCase):
    def test_00_AntivirusUpdateStarted(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateStarted
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateStarted')
        self.assertEqual(value.dump(), 'AntivirusUpdateStarted')
        self.assertEqual(value.get_name(), 'AntivirusUpdateStarted')
        self.assertEqual(value.get_value(), 0)

    def test_01_AntivirusUpdateChecking(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateChecking
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateChecking')
        self.assertEqual(value.dump(), 'AntivirusUpdateChecking')
        self.assertEqual(value.get_name(), 'AntivirusUpdateChecking')
        self.assertEqual(value.get_value(), 1)

    def test_02_AntivirusUpdateDownload(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateDownload
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateDownload')
        self.assertEqual(value.dump(), 'AntivirusUpdateDownload')
        self.assertEqual(value.get_name(), 'AntivirusUpdateDownload')
        self.assertEqual(value.get_value(), 2)

    def test_03_AntivirusUpdateDownloadEngine(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateDownloadEngine
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateDownloadEngine')
        self.assertEqual(value.dump(), 'AntivirusUpdateDownloadEngine')
        self.assertEqual(value.get_name(), 'AntivirusUpdateDownloadEngine')
        self.assertEqual(value.get_value(), 3)

    def test_04_AntivirusUpdateOk(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateOk
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateOk')
        self.assertEqual(value.dump(), 'AntivirusUpdateOk')
        self.assertEqual(value.get_name(), 'AntivirusUpdateOk')
        self.assertEqual(value.get_value(), 4)

    def test_05_AntivirusUpdateFailed(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateFailed
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateFailed')
        self.assertEqual(value.dump(), 'AntivirusUpdateFailed')
        self.assertEqual(value.get_name(), 'AntivirusUpdateFailed')
        self.assertEqual(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test AntivirusUpdatePhases with FAIL
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
