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


class TestCase_MacFilterActionType(unittest.TestCase):
    def test_00_MacFilterDeny(self):
        """
        Test MacFilterActionType with MacFilterDeny
        """
        value = pykerio.enums.MacFilterActionType(name='MacFilterDeny')
        self.assertEqual(value.dump(), 'MacFilterDeny')
        self.assertEqual(value.get_name(), 'MacFilterDeny')
        self.assertEqual(value.get_value(), 0)

    def test_01_MacFilterAllow(self):
        """
        Test MacFilterActionType with MacFilterAllow
        """
        value = pykerio.enums.MacFilterActionType(name='MacFilterAllow')
        self.assertEqual(value.dump(), 'MacFilterAllow')
        self.assertEqual(value.get_name(), 'MacFilterAllow')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test MacFilterActionType with FAIL
        """
        value = pykerio.enums.MacFilterActionType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
