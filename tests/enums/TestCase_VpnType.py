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


class TestCase_VpnType(unittest.TestCase):
    def test_00_VpnType_VpnKerio(self):
        """
        Test VpnType with VpnKerio
        """
        value = pykerio.enums.VpnType(name='VpnKerio')
        self.assertEquals(value.dump(), 'VpnKerio')
        self.assertEquals(value.get_name(), 'VpnKerio')
        self.assertEquals(value.get_value(), 0)

    def test_01_VpnType_VpnIpsec(self):
        """
        Test VpnType with VpnIpsec
        """
        value = pykerio.enums.VpnType(name='VpnIpsec')
        self.assertEquals(value.dump(), 'VpnIpsec')
        self.assertEquals(value.get_name(), 'VpnIpsec')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_VpnType_FAIL(self):
        """
        Test VpnType with FAIL
        """
        value = pykerio.enums.VpnType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
