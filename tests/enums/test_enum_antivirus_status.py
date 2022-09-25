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


class TestCase_AntivirusStatus(unittest.TestCase):
    def test_00_AntivirusOk(self):
        """
        Test AntivirusStatus with AntivirusOk
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusOk')
        self.assertEqual(value.dump(), 'AntivirusOk')
        self.assertEqual(value.get_name(), 'AntivirusOk')
        self.assertEqual(value.get_value(), 0)

    def test_01_AntivirusNotActive(self):
        """
        Test AntivirusStatus with AntivirusNotActive
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusNotActive')
        self.assertEqual(value.dump(), 'AntivirusNotActive')
        self.assertEqual(value.get_name(), 'AntivirusNotActive')
        self.assertEqual(value.get_value(), 1)

    def test_02_AntivirusInternalFailed(self):
        """
        Test AntivirusStatus with AntivirusInternalFailed
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusInternalFailed')
        self.assertEqual(value.dump(), 'AntivirusInternalFailed')
        self.assertEqual(value.get_name(), 'AntivirusInternalFailed')
        self.assertEqual(value.get_value(), 2)

    def test_03_AntivirusExternalFailed(self):
        """
        Test AntivirusStatus with AntivirusExternalFailed
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusExternalFailed')
        self.assertEqual(value.dump(), 'AntivirusExternalFailed')
        self.assertEqual(value.get_name(), 'AntivirusExternalFailed')
        self.assertEqual(value.get_value(), 3)

    def test_04_AntivirusBothFailed(self):
        """
        Test AntivirusStatus with AntivirusBothFailed
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusBothFailed')
        self.assertEqual(value.dump(), 'AntivirusBothFailed')
        self.assertEqual(value.get_name(), 'AntivirusBothFailed')
        self.assertEqual(value.get_value(), 4)

    def test_05_AntivirusWaitingForInitialDb(self):
        """
        Test AntivirusStatus with AntivirusWaitingForInitialDb
        """
        value = pykerio.enums.AntivirusStatus(name='AntivirusWaitingForInitialDb')
        self.assertEqual(value.dump(), 'AntivirusWaitingForInitialDb')
        self.assertEqual(value.get_name(), 'AntivirusWaitingForInitialDb')
        self.assertEqual(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test AntivirusStatus with FAIL
        """
        value = pykerio.enums.AntivirusStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
