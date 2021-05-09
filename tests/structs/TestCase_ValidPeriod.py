##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
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


class TestCase_VpnRoute(unittest.TestCase):
    def test_01_VpnRoute(self):
        """
        Test VpnRoute
        """

        validFromDate = pykerio.structs.Date(
            {'year': 2021, 'month': 5, 'day': 9})
        validFromTime = pykerio.structs.Time({'hour': 0, 'min': 1})
        validToDate = pykerio.structs.Date(
            {'year': 2022, 'month': 5, 'day': 8})
        validToTime = pykerio.structs.Time({'hour': 23, 'min': 59})

        validType = pykerio.enums.ValidType('Valid')

        teststruct = pykerio.structs.ValidPeriod({'validFromDate': validFromDate,
                                                  'validFromTime': validFromTime,
                                                  'validToDate': validToDate,
                                                  'validToTime': validToTime,
                                                  'validType': validType})
        self.assertEquals(len(teststruct.keys()), 5)
        self.assertEquals(len(teststruct.values()), 5)

        self.assertEquals(teststruct['validFromDate'], validFromDate)
        self.assertEquals(teststruct['validFromTime'], validFromTime)
        self.assertEquals(teststruct['validToDate'], validToDate)
        self.assertEquals(teststruct['validToTime'], validToTime)
        self.assertEquals(teststruct['validType'], validType)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
