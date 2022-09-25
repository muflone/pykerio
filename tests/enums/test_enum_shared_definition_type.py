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

from pykerio.enums import SharedDefinitionType


class TestCase_SharedDefinitionType(unittest.TestCase):
    def test_00_SharedDefinitionIpAddrGroup(self):
        """
        Test SharedDefinitionType with SharedDefinitionIpAddrGroup
        """
        value = SharedDefinitionType.SharedDefinitionIpAddrGroup
        self.assertEqual(value.dump(), 'SharedDefinitionIpAddrGroup')
        self.assertEqual(value.name, 'SharedDefinitionIpAddrGroup')
        self.assertEqual(value.value, 0)

    def test_01_SharedDefinitionUrlGroup(self):
        """
        Test SharedDefinitionType with SharedDefinitionUrlGroup
        """
        value = SharedDefinitionType.SharedDefinitionUrlGroup
        self.assertEqual(value.dump(), 'SharedDefinitionUrlGroup')
        self.assertEqual(value.name, 'SharedDefinitionUrlGroup')
        self.assertEqual(value.value, 1)

    def test_02_SharedDefinitionTimeRange(self):
        """
        Test SharedDefinitionType with SharedDefinitionTimeRange
        """
        value = SharedDefinitionType.SharedDefinitionTimeRange
        self.assertEqual(value.dump(), 'SharedDefinitionTimeRange')
        self.assertEqual(value.name, 'SharedDefinitionTimeRange')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test SharedDefinitionType with FAIL
        """
        value = SharedDefinitionType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
