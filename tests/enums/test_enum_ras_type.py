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

from pykerio.enums import RasType


class TestCase_RasType(unittest.TestCase):
    def test_00_PPPoE(self):
        """
        Test RasType with PPPoE
        """
        value = RasType.PPPoE
        self.assertEqual(value.dump(), 'PPPoE')
        self.assertEqual(value.name, 'PPPoE')
        self.assertEqual(value.value, 0)

    def test_01_PPTP(self):
        """
        Test RasType with PPTP
        """
        value = RasType.PPTP
        self.assertEqual(value.dump(), 'PPTP')
        self.assertEqual(value.name, 'PPTP')
        self.assertEqual(value.value, 1)

    def test_02_L2TP(self):
        """
        Test RasType with L2TP
        """
        value = RasType.L2TP
        self.assertEqual(value.dump(), 'L2TP')
        self.assertEqual(value.name, 'L2TP')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test RasType with FAIL
        """
        value = RasType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
