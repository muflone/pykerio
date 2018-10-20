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


class TestCase_PortConfig(unittest.TestCase):
    def test_01_PortConfig(self):
        """
        Test PortConfig
        """
        kid = pykerio.types.KId('port1')
        vlans = pykerio.structs.OptionalString({'enabled': True,
                                                'value': '0'})
        speedDuplexMayNotWork = pykerio.lists.SpeedDuplexMayNotWorkList()
        speedDuplexMayNotWork.append(pykerio.enums.SpeedDuplexType(
            name='SpeedDuplexHalf10'))
        speedDuplexMayNotWork.append(pykerio.enums.SpeedDuplexType(
            name='SpeedDuplexFull10'))

        teststruct = pykerio.structs.PortConfig({
            'id': kid,
            'type': pykerio.enums.PortType('PortEthernet'),
            'name': 'eth0',
            'assignment': pykerio.enums.PortAssignmentType(
                'PortAssignmentStandalone'),
            'vlans': vlans,
            'speedDuplex': pykerio.enums.SpeedDuplexType('SpeedDuplexAuto'),
            'speedDuplexMayNotWork': speedDuplexMayNotWork})

        self.assertEquals(len(teststruct.keys()), 7)
        self.assertEquals(len(teststruct.values()), 7)

        self.assertEquals(teststruct['id'], kid)
        self.assertEquals(teststruct['vlans'], vlans)
        self.assertEquals(teststruct['speedDuplexMayNotWork'],
                          speedDuplexMayNotWork)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
