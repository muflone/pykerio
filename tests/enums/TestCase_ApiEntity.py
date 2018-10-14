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


class TestCase_ApiEntity(unittest.TestCase):
    def test_00_ApiEntity_PolicyWizard(self):
        """
        Test ApiEntity with PolicyWizard
        """
        value = pykerio.enums.ApiEntity(name='PolicyWizard')
        self.assertEquals(value.dump(), 'PolicyWizard')
        self.assertEquals(value.get_name(), 'PolicyWizard')
        self.assertEquals(value.get_value(), 0)

    def test_01_ApiEntity_AlertList(self):
        """
        Test ApiEntity with AlertList
        """
        value = pykerio.enums.ApiEntity(name='AlertList')
        self.assertEquals(value.dump(), 'AlertList')
        self.assertEquals(value.get_name(), 'AlertList')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_ApiEntity_FAIL(self):
        """
        Test ApiEntity with FAIL
        """
        value = pykerio.enums.ApiEntity(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
