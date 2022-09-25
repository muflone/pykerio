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

from pykerio.enums import ConnectivityType


class TestCase_ConnectivityType(unittest.TestCase):
    def test_00_Persistent(self):
        """
        Test ConnectivityType with Persistent
        """
        value = ConnectivityType.Persistent
        self.assertEqual(value.dump(), 'Persistent')
        self.assertEqual(value.name, 'Persistent')
        self.assertEqual(value.value, 0)

    def test_01_DialOnDemand(self):
        """
        Test ConnectivityType with DialOnDemand
        """
        value = ConnectivityType.DialOnDemand
        self.assertEqual(value.dump(), 'DialOnDemand')
        self.assertEqual(value.name, 'DialOnDemand')
        self.assertEqual(value.value, 1)

    def test_02_Failover(self):
        """
        Test ConnectivityType with Failover
        """
        value = ConnectivityType.Failover
        self.assertEqual(value.dump(), 'Failover')
        self.assertEqual(value.name, 'Failover')
        self.assertEqual(value.value, 2)

    def test_03_LoadBalancing(self):
        """
        Test ConnectivityType with LoadBalancing
        """
        value = ConnectivityType.LoadBalancing
        self.assertEqual(value.dump(), 'LoadBalancing')
        self.assertEqual(value.name, 'LoadBalancing')
        self.assertEqual(value.value, 3)
