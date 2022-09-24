##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2022 Fabio Castelli
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


class TestCase_NatBalancing(unittest.TestCase):
    def test_00_NatBalancing_BalancingPerHost(self):
        """
        Test NatBalancing with BalancingPerHost
        """
        value = pykerio.enums.NatBalancing(name='BalancingPerHost')
        self.assertEquals(value.dump(), 'BalancingPerHost')
        self.assertEquals(value.get_name(), 'BalancingPerHost')
        self.assertEquals(value.get_value(), 0)

    def test_01_NatBalancing_BalancingPerConnection(self):
        """
        Test NatBalancing with BalancingPerConnection
        """
        value = pykerio.enums.NatBalancing(name='BalancingPerConnection')
        self.assertEquals(value.dump(), 'BalancingPerConnection')
        self.assertEquals(value.get_name(), 'BalancingPerConnection')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_NatBalancing_FAIL(self):
        """
        Test NatBalancing with FAIL
        """
        value = pykerio.enums.NatBalancing(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
