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


class TestCase_DateTimeConfig(unittest.TestCase):
    def test_01_DateTimeConfig(self):
        """
        Test DateTimeConfig
        """
        year = 2018
        month = 10
        day = 7
        date = pykerio.structs.Date({'year': year,
                                     'month': month,
                                     'day': day})
        hour = 12
        minutes = 34
        seconds = 56
        timehms = pykerio.structs.TimeHMS({'hour': hour,
                                           'min': minutes,
                                           'sec': seconds})
        teststruct = pykerio.structs.DateTimeConfig({'date': date,
                                                     'time': timehms})
        self.assertEquals(len(teststruct.keys()), 2)
        self.assertEquals(len(teststruct.values()), 2)

        self.assertEquals(teststruct['date'], date)
        self.assertEquals(teststruct['time'], timehms)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
