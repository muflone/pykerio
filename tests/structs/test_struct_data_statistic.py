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


class TestCase_DataStatistic(unittest.TestCase):
    def test_01_DataStatistic(self):
        """
        Test DataStatistic
        """
        counter = 123456.0
        counterIn = 100000.0
        counterOut = 23456.0
        teststruct = pykerio.structs.DataStatistic({'today': counter,
                                                    'todayIn': counterIn,
                                                    'todayOut': counterOut,
                                                    'week': counter,
                                                    'weekIn': counterIn,
                                                    'weekOut': counterOut,
                                                    'month': counter,
                                                    'monthIn': counterIn,
                                                    'monthOut': counterOut,
                                                    'total': counter,
                                                    'totalIn': counterIn,
                                                    'totalOut': counterOut})
        self.assertEqual(len(teststruct.keys()), 12)
        self.assertEqual(len(teststruct.values()), 12)

        self.assertEqual(teststruct['today'], counter)
        self.assertEqual(teststruct['todayIn'], counterIn)
        self.assertEqual(teststruct['todayOut'], counterOut)
        self.assertEqual(teststruct['week'], counter)
        self.assertEqual(teststruct['weekIn'], counterIn)
        self.assertEqual(teststruct['weekOut'], counterOut)
        self.assertEqual(teststruct['month'], counter)
        self.assertEqual(teststruct['monthIn'], counterIn)
        self.assertEqual(teststruct['monthOut'], counterOut)
        self.assertEqual(teststruct['total'], counter)
        self.assertEqual(teststruct['totalIn'], counterIn)
        self.assertEqual(teststruct['totalOut'], counterOut)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
