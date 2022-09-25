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

from pykerio.enums import IpVersion


class TestCase_IpVersion(unittest.TestCase):
    def test_00_IpVersion4(self):
        """
        Test IpVersion with IpVersion4
        """
        value = IpVersion.IpVersion4
        self.assertEqual(value.dump(), 'IpVersion4')
        self.assertEqual(value.name, 'IpVersion4')
        self.assertEqual(value.value, 0)

    def test_01_IpVersion6(self):
        """
        Test IpVersion with IpVersion6
        """
        value = IpVersion.IpVersion6
        self.assertEqual(value.dump(), 'IpVersion6')
        self.assertEqual(value.name, 'IpVersion6')
        self.assertEqual(value.value, 1)

    def test_02_IpVersionAny(self):
        """
        Test IpVersion with IpVersionAny
        """
        value = IpVersion.IpVersionAny
        self.assertEqual(value.dump(), 'IpVersionAny')
        self.assertEqual(value.name, 'IpVersionAny')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test IpVersion with FAIL
        """
        value = IpVersion.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
