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


class TestCase_ConnectivityType(unittest.TestCase):
    def test_00_ConnectivityType_Persistent(self):
        """
        Test ConnectivityType with Persistent
        """
        value = pykerio.enums.ConnectivityType(name='Persistent')
        self.assertEquals(value.dump(), 'Persistent')
        self.assertEquals(value.get_name(), 'Persistent')
        self.assertEquals(value.get_value(), 0)

    def test_01_ConnectivityType_DialOnDemand(self):
        """
        Test ConnectivityType with DialOnDemand
        """
        value = pykerio.enums.ConnectivityType(name='DialOnDemand')
        self.assertEquals(value.dump(), 'DialOnDemand')
        self.assertEquals(value.get_name(), 'DialOnDemand')
        self.assertEquals(value.get_value(), 1)

    def test_02_ConnectivityType_Failover(self):
        """
        Test ConnectivityType with Failover
        """
        value = pykerio.enums.ConnectivityType(name='Failover')
        self.assertEquals(value.dump(), 'Failover')
        self.assertEquals(value.get_name(), 'Failover')
        self.assertEquals(value.get_value(), 2)

    def test_03_ConnectivityType_LoadBalancing(self):
        """
        Test ConnectivityType with LoadBalancing
        """
        value = pykerio.enums.ConnectivityType(name='LoadBalancing')
        self.assertEquals(value.dump(), 'LoadBalancing')
        self.assertEquals(value.get_name(), 'LoadBalancing')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_ConnectivityType_FAIL(self):
        """
        Test ConnectivityType with FAIL
        """
        value = pykerio.enums.ConnectivityType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
