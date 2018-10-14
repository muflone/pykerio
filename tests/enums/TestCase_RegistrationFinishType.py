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


class TestCase_RegistrationFinishType(unittest.TestCase):
    def test_00_RegistrationFinishType_rfCreate(self):
        """
        Test RegistrationFinishType with rfCreate
        """
        value = pykerio.enums.RegistrationFinishType(name='rfCreate')
        self.assertEquals(value.dump(), 'rfCreate')
        self.assertEquals(value.get_name(), 'rfCreate')
        self.assertEquals(value.get_value(), 0)

    def test_01_RegistrationFinishType_rfModify(self):
        """
        Test RegistrationFinishType with rfModify
        """
        value = pykerio.enums.RegistrationFinishType(name='rfModify')
        self.assertEquals(value.dump(), 'rfModify')
        self.assertEquals(value.get_name(), 'rfModify')
        self.assertEquals(value.get_value(), 1)

    def test_02_RegistrationFinishType_rfDownload(self):
        """
        Test RegistrationFinishType with rfDownload
        """
        value = pykerio.enums.RegistrationFinishType(name='rfDownload')
        self.assertEquals(value.dump(), 'rfDownload')
        self.assertEquals(value.get_name(), 'rfDownload')
        self.assertEquals(value.get_value(), 2)

    def test_03_RegistrationFinishType_rfStore(self):
        """
        Test RegistrationFinishType with rfStore
        """
        value = pykerio.enums.RegistrationFinishType(name='rfStore')
        self.assertEquals(value.dump(), 'rfStore')
        self.assertEquals(value.get_name(), 'rfStore')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_RegistrationFinishType_FAIL(self):
        """
        Test RegistrationFinishType with FAIL
        """
        value = pykerio.enums.RegistrationFinishType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
