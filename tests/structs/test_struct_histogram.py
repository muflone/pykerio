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


class TestCase_Histogram(unittest.TestCase):
    def test_01_Histogram(self):
        """
        Test Histogram
        """
        speed = 100000.0
        units = pykerio.enums.ByteUnits.GigaBytes
        histogramdata = pykerio.structs.HistogramData({'inbound': speed,
                                                       'outbound': speed})
        testlist = pykerio.lists.HistogramDataList()
        testlist.append(histogramdata)
        teststruct = pykerio.structs.Histogram({'units': units,
                                                'averageIn': speed,
                                                'averageOut': speed,
                                                'maxIn': speed,
                                                'maxOut': speed,
                                                'data': testlist})
        self.assertEqual(len(teststruct.keys()), 6)
        self.assertEqual(len(teststruct.values()), 6)

        self.assertEqual(teststruct['units'], units)
        self.assertEqual(teststruct['averageIn'], speed)
        self.assertEqual(teststruct['averageOut'], speed)
        self.assertEqual(teststruct['maxIn'], speed)
        self.assertEqual(teststruct['maxOut'], speed)
        self.assertEqual(teststruct['data'], testlist)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
