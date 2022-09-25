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

from pykerio.enums import TrafficStatisticsType


class TestCase_TrafficStatisticsType(unittest.TestCase):
    def test_00_TrafficStatisticsInterface(self):
        """
        Test TrafficStatisticsType with TrafficStatisticsInterface
        """
        value = TrafficStatisticsType.TrafficStatisticsInterface
        self.assertEqual(value.dump(), 'TrafficStatisticsInterface')
        self.assertEqual(value.name, 'TrafficStatisticsInterface')
        self.assertEqual(value.value, 0)

    def test_01_TrafficStatisticsTrafficRule(self):
        """
        Test TrafficStatisticsType with TrafficStatisticsTrafficRule
        """
        value = TrafficStatisticsType.TrafficStatisticsTrafficRule
        self.assertEqual(value.dump(), 'TrafficStatisticsTrafficRule')
        self.assertEqual(value.name, 'TrafficStatisticsTrafficRule')
        self.assertEqual(value.value, 1)

    def test_02_TrafficStatisticsBandwidthRule(self):
        """
        Test TrafficStatisticsType with TrafficStatisticsBandwidthRule
        """
        value = TrafficStatisticsType.TrafficStatisticsBandwidthRule
        self.assertEqual(value.dump(), 'TrafficStatisticsBandwidthRule')
        self.assertEqual(value.name, 'TrafficStatisticsBandwidthRule')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test TrafficStatisticsType with FAIL
        """
        value = TrafficStatisticsType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
