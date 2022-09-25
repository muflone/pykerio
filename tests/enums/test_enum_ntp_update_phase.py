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


class TestCase_NtpUpdatePhase(unittest.TestCase):
    def test_00_NtpUpdateDisabled(self):
        """
        Test NtpUpdatePhase with NtpUpdateDisabled
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateDisabled')
        self.assertEqual(value.dump(), 'NtpUpdateDisabled')
        self.assertEqual(value.get_name(), 'NtpUpdateDisabled')
        self.assertEqual(value.get_value(), 0)

    def test_01_NtpUpdateOk(self):
        """
        Test NtpUpdatePhase with NtpUpdateOk
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateOk')
        self.assertEqual(value.dump(), 'NtpUpdateOk')
        self.assertEqual(value.get_name(), 'NtpUpdateOk')
        self.assertEqual(value.get_value(), 1)

    def test_02_NtpUpdateError(self):
        """
        Test NtpUpdatePhase with NtpUpdateError
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateError')
        self.assertEqual(value.dump(), 'NtpUpdateError')
        self.assertEqual(value.get_name(), 'NtpUpdateError')
        self.assertEqual(value.get_value(), 2)

    def test_03_NtpUpdateProgress(self):
        """
        Test NtpUpdatePhase with NtpUpdateProgress
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateProgress')
        self.assertEqual(value.dump(), 'NtpUpdateProgress')
        self.assertEqual(value.get_name(), 'NtpUpdateProgress')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test NtpUpdatePhase with FAIL
        """
        value = pykerio.enums.NtpUpdatePhase(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
