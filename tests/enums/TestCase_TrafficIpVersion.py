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


class TestCase_TrafficIpVersion(unittest.TestCase):
    def test_00_TrafficIpVersion_Ipv4(self):
        """
        Test TrafficIpVersion with Ipv4
        """
        value = pykerio.enums.TrafficIpVersion(name='Ipv4')
        self.assertEquals(value.dump(), 'Ipv4')
        self.assertEquals(value.get_name(), 'Ipv4')
        self.assertEquals(value.get_value(), 0)

    def test_01_TrafficIpVersion_Ipv6(self):
        """
        Test TrafficIpVersion with Ipv6
        """
        value = pykerio.enums.TrafficIpVersion(name='Ipv6')
        self.assertEquals(value.dump(), 'Ipv6')
        self.assertEquals(value.get_name(), 'Ipv6')
        self.assertEquals(value.get_value(), 1)

    def test_02_TrafficIpVersion_IpAll(self):
        """
        Test TrafficIpVersion with IpAll
        """
        value = pykerio.enums.TrafficIpVersion(name='IpAll')
        self.assertEquals(value.dump(), 'IpAll')
        self.assertEquals(value.get_name(), 'IpAll')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_TrafficIpVersion_FAIL(self):
        """
        Test TrafficIpVersion with FAIL
        """
        value = pykerio.enums.TrafficIpVersion(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
