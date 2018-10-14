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
        self.assertEquals(len(teststruct.keys()), 12)
        self.assertEquals(len(teststruct.values()), 12)

        self.assertEquals(teststruct['today'], counter)
        self.assertEquals(teststruct['todayIn'], counterIn)
        self.assertEquals(teststruct['todayOut'], counterOut)
        self.assertEquals(teststruct['week'], counter)
        self.assertEquals(teststruct['weekIn'], counterIn)
        self.assertEquals(teststruct['weekOut'], counterOut)
        self.assertEquals(teststruct['month'], counter)
        self.assertEquals(teststruct['monthIn'], counterIn)
        self.assertEquals(teststruct['monthOut'], counterOut)
        self.assertEquals(teststruct['total'], counter)
        self.assertEquals(teststruct['totalIn'], counterIn)
        self.assertEquals(teststruct['totalOut'], counterOut)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
