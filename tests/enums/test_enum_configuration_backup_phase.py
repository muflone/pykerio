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

from pykerio.enums import ConfigurationBackupPhase


class TestCase_ConfigurationBackupPhase(unittest.TestCase):
    def test_00_ConfigurationBackupOk(self):
        """
        Test ConfigurationBackupPhase with ConfigurationBackupOk
        """
        value = ConfigurationBackupPhase.ConfigurationBackupOk
        self.assertEqual(value.dump(), 'ConfigurationBackupOk')
        self.assertEqual(value.name, 'ConfigurationBackupOk')
        self.assertEqual(value.value, 0)

    def test_01_ConfigurationBackupInProgress(self):
        """
        Test ConfigurationBackupPhase with ConfigurationBackupInProgress
        """
        value = ConfigurationBackupPhase.ConfigurationBackupInProgress
        self.assertEqual(value.dump(), 'ConfigurationBackupInProgress')
        self.assertEqual(value.name, 'ConfigurationBackupInProgress')
        self.assertEqual(value.value, 1)

    def test_02_ConfigurationBackupFailed(self):
        """
        Test ConfigurationBackupPhase with ConfigurationBackupFailed
        """
        value = ConfigurationBackupPhase.ConfigurationBackupFailed
        self.assertEqual(value.dump(), 'ConfigurationBackupFailed')
        self.assertEqual(value.name, 'ConfigurationBackupFailed')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ConfigurationBackupPhase with FAIL
        """
        value = ConfigurationBackupPhase.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
