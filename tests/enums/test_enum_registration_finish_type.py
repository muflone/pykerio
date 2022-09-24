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


class TestCase_RegistrationFinishType(unittest.TestCase):
    def test_00_RegistrationFinishType_rfCreate(self):
        """
        Test RegistrationFinishType with rfCreate
        """
        value = pykerio.enums.RegistrationFinishType(name='rfCreate')
        self.assertEqual(value.dump(), 'rfCreate')
        self.assertEqual(value.get_name(), 'rfCreate')
        self.assertEqual(value.get_value(), 0)

    def test_01_RegistrationFinishType_rfModify(self):
        """
        Test RegistrationFinishType with rfModify
        """
        value = pykerio.enums.RegistrationFinishType(name='rfModify')
        self.assertEqual(value.dump(), 'rfModify')
        self.assertEqual(value.get_name(), 'rfModify')
        self.assertEqual(value.get_value(), 1)

    def test_02_RegistrationFinishType_rfDownload(self):
        """
        Test RegistrationFinishType with rfDownload
        """
        value = pykerio.enums.RegistrationFinishType(name='rfDownload')
        self.assertEqual(value.dump(), 'rfDownload')
        self.assertEqual(value.get_name(), 'rfDownload')
        self.assertEqual(value.get_value(), 2)

    def test_03_RegistrationFinishType_rfStore(self):
        """
        Test RegistrationFinishType with rfStore
        """
        value = pykerio.enums.RegistrationFinishType(name='rfStore')
        self.assertEqual(value.dump(), 'rfStore')
        self.assertEqual(value.get_name(), 'rfStore')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_RegistrationFinishType_FAIL(self):
        """
        Test RegistrationFinishType with FAIL
        """
        value = pykerio.enums.RegistrationFinishType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
