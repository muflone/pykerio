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

from pykerio.enums import RegistrationFinishType


class TestCase_RegistrationFinishType(unittest.TestCase):
    def test_00_rfCreate(self):
        """
        Test RegistrationFinishType with rfCreate
        """
        value = RegistrationFinishType.rfCreate
        self.assertEqual(value.dump(), 'rfCreate')
        self.assertEqual(value.name, 'rfCreate')
        self.assertEqual(value.value, 0)

    def test_01_rfModify(self):
        """
        Test RegistrationFinishType with rfModify
        """
        value = RegistrationFinishType.rfModify
        self.assertEqual(value.dump(), 'rfModify')
        self.assertEqual(value.name, 'rfModify')
        self.assertEqual(value.value, 1)

    def test_02_rfDownload(self):
        """
        Test RegistrationFinishType with rfDownload
        """
        value = RegistrationFinishType.rfDownload
        self.assertEqual(value.dump(), 'rfDownload')
        self.assertEqual(value.name, 'rfDownload')
        self.assertEqual(value.value, 2)

    def test_03_rfStore(self):
        """
        Test RegistrationFinishType with rfStore
        """
        value = RegistrationFinishType.rfStore
        self.assertEqual(value.dump(), 'rfStore')
        self.assertEqual(value.name, 'rfStore')
        self.assertEqual(value.value, 3)
