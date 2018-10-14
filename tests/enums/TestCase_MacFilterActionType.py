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


class TestCase_MacFilterActionType(unittest.TestCase):
    def test_00_MacFilterActionType_MacFilterDeny(self):
        """
        Test MacFilterActionType with MacFilterDeny
        """
        value = pykerio.enums.MacFilterActionType(name='MacFilterDeny')
        self.assertEquals(value.dump(), 'MacFilterDeny')
        self.assertEquals(value.get_name(), 'MacFilterDeny')
        self.assertEquals(value.get_value(), 0)

    def test_01_MacFilterActionType_MacFilterAllow(self):
        """
        Test MacFilterActionType with MacFilterAllow
        """
        value = pykerio.enums.MacFilterActionType(name='MacFilterAllow')
        self.assertEquals(value.dump(), 'MacFilterAllow')
        self.assertEquals(value.get_name(), 'MacFilterAllow')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_MacFilterActionType_FAIL(self):
        """
        Test MacFilterActionType with FAIL
        """
        value = pykerio.enums.MacFilterActionType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
