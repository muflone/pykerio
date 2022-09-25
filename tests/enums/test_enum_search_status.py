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

from pykerio.enums import SearchStatus


class TestCase_SearchStatus(unittest.TestCase):
    def test_00_ResultFound(self):
        """
        Test SearchStatus with ResultFound
        """
        value = SearchStatus.ResultFound
        self.assertEqual(value.dump(), 'ResultFound')
        self.assertEqual(value.name, 'ResultFound')
        self.assertEqual(value.value, 0)

    def test_01_Searching(self):
        """
        Test SearchStatus with Searching
        """
        value = SearchStatus.Searching
        self.assertEqual(value.dump(), 'Searching')
        self.assertEqual(value.name, 'Searching')
        self.assertEqual(value.value, 1)

    def test_02_Cancelled(self):
        """
        Test SearchStatus with Cancelled
        """
        value = SearchStatus.Cancelled
        self.assertEqual(value.dump(), 'Cancelled')
        self.assertEqual(value.name, 'Cancelled')
        self.assertEqual(value.value, 2)

    def test_03_ResultNotFound(self):
        """
        Test SearchStatus with ResultNotFound
        """
        value = SearchStatus.ResultNotFound
        self.assertEqual(value.dump(), 'ResultNotFound')
        self.assertEqual(value.name, 'ResultNotFound')
        self.assertEqual(value.value, 3)
