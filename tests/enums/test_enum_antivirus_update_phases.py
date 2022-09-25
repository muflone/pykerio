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

from pykerio.enums import AntivirusUpdatePhases


class TestCase_AntivirusUpdatePhases(unittest.TestCase):
    def test_00_AntivirusUpdateStarted(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateStarted
        """
        value = AntivirusUpdatePhases.AntivirusUpdateStarted
        self.assertEqual(value.dump(), 'AntivirusUpdateStarted')
        self.assertEqual(value.name, 'AntivirusUpdateStarted')
        self.assertEqual(value.value, 0)

    def test_01_AntivirusUpdateChecking(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateChecking
        """
        value = AntivirusUpdatePhases.AntivirusUpdateChecking
        self.assertEqual(value.dump(), 'AntivirusUpdateChecking')
        self.assertEqual(value.name, 'AntivirusUpdateChecking')
        self.assertEqual(value.value, 1)

    def test_02_AntivirusUpdateDownload(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateDownload
        """
        value = AntivirusUpdatePhases.AntivirusUpdateDownload
        self.assertEqual(value.dump(), 'AntivirusUpdateDownload')
        self.assertEqual(value.name, 'AntivirusUpdateDownload')
        self.assertEqual(value.value, 2)

    def test_03_AntivirusUpdateDownloadEngine(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateDownloadEngine
        """
        value = AntivirusUpdatePhases.AntivirusUpdateDownloadEngine
        self.assertEqual(value.dump(), 'AntivirusUpdateDownloadEngine')
        self.assertEqual(value.name, 'AntivirusUpdateDownloadEngine')
        self.assertEqual(value.value, 3)

    def test_04_AntivirusUpdateOk(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateOk
        """
        value = AntivirusUpdatePhases.AntivirusUpdateOk
        self.assertEqual(value.dump(), 'AntivirusUpdateOk')
        self.assertEqual(value.name, 'AntivirusUpdateOk')
        self.assertEqual(value.value, 4)

    def test_05_AntivirusUpdateFailed(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateFailed
        """
        value = AntivirusUpdatePhases.AntivirusUpdateFailed
        self.assertEqual(value.dump(), 'AntivirusUpdateFailed')
        self.assertEqual(value.name, 'AntivirusUpdateFailed')
        self.assertEqual(value.value, 5)
