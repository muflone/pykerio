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


class TestCase_NatBalancing(unittest.TestCase):
    def test_00_NatBalancing_BalancingPerHost(self):
        """
        Test NatBalancing with BalancingPerHost
        """
        value = pykerio.enums.NatBalancing(name='BalancingPerHost')
        self.assertEqual(value.dump(), 'BalancingPerHost')
        self.assertEqual(value.get_name(), 'BalancingPerHost')
        self.assertEqual(value.get_value(), 0)

    def test_01_NatBalancing_BalancingPerConnection(self):
        """
        Test NatBalancing with BalancingPerConnection
        """
        value = pykerio.enums.NatBalancing(name='BalancingPerConnection')
        self.assertEqual(value.dump(), 'BalancingPerConnection')
        self.assertEqual(value.get_name(), 'BalancingPerConnection')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_NatBalancing_FAIL(self):
        """
        Test NatBalancing with FAIL
        """
        value = pykerio.enums.NatBalancing(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
