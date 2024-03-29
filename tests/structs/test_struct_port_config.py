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
from pykerio.enums import (PortAssignmentType,
                           PortType,
                           SpeedDuplexType)


class TestCase_PortConfig(unittest.TestCase):
    def test_01_PortConfig(self):
        """
        Test PortConfig
        """
        kid = pykerio.types.KId('port1')
        vlans = pykerio.structs.OptionalString({'enabled': True,
                                                'value': '0'})
        speedDuplexMayNotWork = pykerio.lists.SpeedDuplexMayNotWorkList()
        speedDuplexMayNotWork.append(SpeedDuplexType.SpeedDuplexHalf10)
        speedDuplexMayNotWork.append(SpeedDuplexType.SpeedDuplexFull10)

        teststruct = pykerio.structs.PortConfig({
            'id': kid,
            'type': PortType.PortEthernet,
            'name': 'eth0',
            'assignment': PortAssignmentType.PortAssignmentStandalone,
            'vlans': vlans,
            'speedDuplex': SpeedDuplexType.SpeedDuplexAuto,
            'speedDuplexMayNotWork': speedDuplexMayNotWork})

        self.assertEqual(len(teststruct.keys()), 7)
        self.assertEqual(len(teststruct.values()), 7)

        self.assertEqual(teststruct['id'], kid)
        self.assertEqual(teststruct['vlans'], vlans)
        self.assertEqual(teststruct['speedDuplexMayNotWork'],
                         speedDuplexMayNotWork)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
