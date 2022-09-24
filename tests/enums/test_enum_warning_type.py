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


class TestCase_WarningType(unittest.TestCase):
    def test_00_WarningType_WarnBetaVersion(self):
        """
        Test WarningType with WarnBetaVersion
        """
        value = pykerio.enums.WarningType(name='WarnBetaVersion')
        self.assertEqual(value.dump(), 'WarnBetaVersion')
        self.assertEqual(value.get_name(), 'WarnBetaVersion')
        self.assertEqual(value.get_value(), 0)

    def test_01_WarningType_WarnUpdateFailed(self):
        """
        Test WarningType with WarnUpdateFailed
        """
        value = pykerio.enums.WarningType(name='WarnUpdateFailed')
        self.assertEqual(value.dump(), 'WarnUpdateFailed')
        self.assertEqual(value.get_name(), 'WarnUpdateFailed')
        self.assertEqual(value.get_value(), 1)

    def test_02_WarningType_WarnConfigurationReverted(self):
        """
        Test WarningType with WarnConfigurationReverted
        """
        value = pykerio.enums.WarningType(name='WarnConfigurationReverted')
        self.assertEqual(value.dump(), 'WarnConfigurationReverted')
        self.assertEqual(value.get_name(), 'WarnConfigurationReverted')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_WarningType_FAIL(self):
        """
        Test WarningType with FAIL
        """
        value = pykerio.enums.WarningType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
