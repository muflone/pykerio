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

from pykerio.enums import ConnectionDirection


class TestCase_ConnectionDirection(unittest.TestCase):
    def test_00_ConnectionDirectionInbound(self):
        """
        Test ConnectionDirection with ConnectionDirectionInbound
        """
        value = ConnectionDirection.ConnectionDirectionInbound
        self.assertEqual(value.dump(), 'ConnectionDirectionInbound')
        self.assertEqual(value.name, 'ConnectionDirectionInbound')
        self.assertEqual(value.value, 0)

    def test_01_ConnectionDirectionOutbound(self):
        """
        Test ConnectionDirection with ConnectionDirectionOutbound
        """
        value = ConnectionDirection.ConnectionDirectionOutbound
        self.assertEqual(value.dump(), 'ConnectionDirectionOutbound')
        self.assertEqual(value.name, 'ConnectionDirectionOutbound')
        self.assertEqual(value.value, 1)

    def test_02_ConnectionDirectionLocal(self):
        """
        Test ConnectionDirection with ConnectionDirectionLocal
        """
        value = ConnectionDirection.ConnectionDirectionLocal
        self.assertEqual(value.dump(), 'ConnectionDirectionLocal')
        self.assertEqual(value.name, 'ConnectionDirectionLocal')
        self.assertEqual(value.value, 2)
