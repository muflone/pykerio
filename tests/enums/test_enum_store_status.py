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

from pykerio.enums import StoreStatus


class TestCase_StoreStatus(unittest.TestCase):
    def test_00_StoreStatusClean(self):
        """
        Test StoreStatus with StoreStatusClean
        """
        value = StoreStatus.StoreStatusClean
        self.assertEqual(value.dump(), 'StoreStatusClean')
        self.assertEqual(value.name, 'StoreStatusClean')
        self.assertEqual(value.value, 0)

    def test_01_StoreStatusModified(self):
        """
        Test StoreStatus with StoreStatusModified
        """
        value = StoreStatus.StoreStatusModified
        self.assertEqual(value.dump(), 'StoreStatusModified')
        self.assertEqual(value.name, 'StoreStatusModified')
        self.assertEqual(value.value, 1)

    def test_02_StoreStatusNew(self):
        """
        Test StoreStatus with StoreStatusNew
        """
        value = StoreStatus.StoreStatusNew
        self.assertEqual(value.dump(), 'StoreStatusNew')
        self.assertEqual(value.name, 'StoreStatusNew')
        self.assertEqual(value.value, 2)
