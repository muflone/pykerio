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


class TestCase_HistogramType(unittest.TestCase):
    def test_00_HistogramType_HistogramOneDay(self):
        """
        Test HistogramType with HistogramOneDay
        """
        value = pykerio.enums.HistogramType(name='HistogramOneDay')
        self.assertEquals(value.dump(), 'HistogramOneDay')
        self.assertEquals(value.get_name(), 'HistogramOneDay')
        self.assertEquals(value.get_value(), 0)

    def test_01_HistogramType_HistogramTwoHours(self):
        """
        Test HistogramType with HistogramTwoHours
        """
        value = pykerio.enums.HistogramType(name='HistogramTwoHours')
        self.assertEquals(value.dump(), 'HistogramTwoHours')
        self.assertEquals(value.get_name(), 'HistogramTwoHours')
        self.assertEquals(value.get_value(), 1)

    def test_02_HistogramType_HistogramOneWeek(self):
        """
        Test HistogramType with HistogramOneWeek
        """
        value = pykerio.enums.HistogramType(name='HistogramOneWeek')
        self.assertEquals(value.dump(), 'HistogramOneWeek')
        self.assertEquals(value.get_name(), 'HistogramOneWeek')
        self.assertEquals(value.get_value(), 2)

    def test_03_HistogramType_HistogramOneMonth(self):
        """
        Test HistogramType with HistogramOneMonth
        """
        value = pykerio.enums.HistogramType(name='HistogramOneMonth')
        self.assertEquals(value.dump(), 'HistogramOneMonth')
        self.assertEquals(value.get_name(), 'HistogramOneMonth')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_HistogramType_FAIL(self):
        """
        Test HistogramType with FAIL
        """
        value = pykerio.enums.HistogramType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
