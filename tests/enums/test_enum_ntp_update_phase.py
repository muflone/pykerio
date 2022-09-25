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

from pykerio.enums import NtpUpdatePhase


class TestCase_NtpUpdatePhase(unittest.TestCase):
    def test_00_NtpUpdateDisabled(self):
        """
        Test NtpUpdatePhase with NtpUpdateDisabled
        """
        value = NtpUpdatePhase.NtpUpdateDisabled
        self.assertEqual(value.dump(), 'NtpUpdateDisabled')
        self.assertEqual(value.name, 'NtpUpdateDisabled')
        self.assertEqual(value.value, 0)

    def test_01_NtpUpdateOk(self):
        """
        Test NtpUpdatePhase with NtpUpdateOk
        """
        value = NtpUpdatePhase.NtpUpdateOk
        self.assertEqual(value.dump(), 'NtpUpdateOk')
        self.assertEqual(value.name, 'NtpUpdateOk')
        self.assertEqual(value.value, 1)

    def test_02_NtpUpdateError(self):
        """
        Test NtpUpdatePhase with NtpUpdateError
        """
        value = NtpUpdatePhase.NtpUpdateError
        self.assertEqual(value.dump(), 'NtpUpdateError')
        self.assertEqual(value.name, 'NtpUpdateError')
        self.assertEqual(value.value, 2)

    def test_03_NtpUpdateProgress(self):
        """
        Test NtpUpdatePhase with NtpUpdateProgress
        """
        value = NtpUpdatePhase.NtpUpdateProgress
        self.assertEqual(value.dump(), 'NtpUpdateProgress')
        self.assertEqual(value.name, 'NtpUpdateProgress')
        self.assertEqual(value.value, 3)
