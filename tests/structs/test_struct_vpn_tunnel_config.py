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


class TestCase_VpnTunnelConfig(unittest.TestCase):
    def test_01_VpnTunnelConfig(self):
        """
        Test VpnTunnelConfig
        """
        peer = pykerio.structs.OptionalString({'enabled': True,
                                               'value': 'remote.site'})
        routes = pykerio.lists.VpnRouteList()
        kid = pykerio.types.KId('Route 1')
        description = 'Route LAN'
        network = pykerio.types.IpAddress('192.168.10.0')
        netmask = pykerio.types.IpAddress('255.255.255.0')
        route = pykerio.structs.VpnRoute({'id': kid,
                                          'enabled': True,
                                          'description': description,
                                          'network': network,
                                          'mask': netmask})
        routes.append(route)

        secret = 'secretpassword'
        psk = pykerio.structs.OptionalString({'enabled': True,
                                              'value': secret})
        certificate = pykerio.structs.IdReference({
            'id': pykerio.types.KId('certificate1'),
            'name': 'certificate1',
            'invalid': False})
        network = pykerio.types.IpAddress('192.168.10.0')
        netmask = pykerio.types.IpAddress('255.255.255.0')
        route = pykerio.structs.VpnRoute({'id': pykerio.types.KId('Route 1'),
                                          'enabled': True,
                                          'description': 'Route LAN',
                                          'network': network,
                                          'mask': netmask})
        routes = pykerio.lists.VpnRouteList()
        routes.append(route)

        teststruct = pykerio.structs.VpnTunnelConfig({
            'type': pykerio.enums.VpnType(name='VpnKerio'),
            'peer': peer,
            'localRoutes': routes,
            'remoteRoutes': routes,
            'remoteFingerprint': 'abcdefg',
            'useRemoteAutomaticRoutes': True,
            'useRemoteCustomRoutes': False,
            'psk': psk,
            'certificate': certificate,
            'cipherIke': secret,
            'cipherEsp': secret,
            'localIdValue': '192.168.10.0',
            'remoteIdValue': '192.168.110.0',
            'useLocalAutomaticRoutes': False,
            'useLocalCustomRoutes': False})
        self.assertEqual(len(teststruct.keys()), 15)
        self.assertEqual(len(teststruct.values()), 15)

        self.assertEqual(teststruct['peer'], peer)
        self.assertEqual(teststruct['psk'], psk)
        self.assertEqual(teststruct['cipherIke'], secret)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
