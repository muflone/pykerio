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


class TestCase_AntivirusUpdatePhases(unittest.TestCase):
    def test_00_AntivirusUpdatePhases_AntivirusUpdateStarted(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateStarted
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateStarted')
        self.assertEquals(value.dump(), 'AntivirusUpdateStarted')
        self.assertEquals(value.get_name(), 'AntivirusUpdateStarted')
        self.assertEquals(value.get_value(), 0)

    def test_01_AntivirusUpdatePhases_AntivirusUpdateChecking(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateChecking
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateChecking')
        self.assertEquals(value.dump(), 'AntivirusUpdateChecking')
        self.assertEquals(value.get_name(), 'AntivirusUpdateChecking')
        self.assertEquals(value.get_value(), 1)

    def test_02_AntivirusUpdatePhases_AntivirusUpdateDownload(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateDownload
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateDownload')
        self.assertEquals(value.dump(), 'AntivirusUpdateDownload')
        self.assertEquals(value.get_name(), 'AntivirusUpdateDownload')
        self.assertEquals(value.get_value(), 2)

    def test_03_AntivirusUpdatePhases_AntivirusUpdateDownloadEngine(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateDownloadEngine
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateDownloadEngine')
        self.assertEquals(value.dump(), 'AntivirusUpdateDownloadEngine')
        self.assertEquals(value.get_name(), 'AntivirusUpdateDownloadEngine')
        self.assertEquals(value.get_value(), 3)

    def test_04_AntivirusUpdatePhases_AntivirusUpdateOk(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateOk
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateOk')
        self.assertEquals(value.dump(), 'AntivirusUpdateOk')
        self.assertEquals(value.get_name(), 'AntivirusUpdateOk')
        self.assertEquals(value.get_value(), 4)

    def test_05_AntivirusUpdatePhases_AntivirusUpdateFailed(self):
        """
        Test AntivirusUpdatePhases with AntivirusUpdateFailed
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='AntivirusUpdateFailed')
        self.assertEquals(value.dump(), 'AntivirusUpdateFailed')
        self.assertEquals(value.get_name(), 'AntivirusUpdateFailed')
        self.assertEquals(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_AntivirusUpdatePhases_FAIL(self):
        """
        Test AntivirusUpdatePhases with FAIL
        """
        value = pykerio.enums.AntivirusUpdatePhases(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
