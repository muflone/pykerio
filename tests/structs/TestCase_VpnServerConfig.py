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


class TestCase_VpnServerConfig(unittest.TestCase):
    def test_01_VpnServerConfig(self):
        """
        Test VpnServerConfig
        """
        certificate = pykerio.structs.IdReference({
            'id': pykerio.types.KId('certificate1'),
            'name': 'certificate1',
            'invalid': False})
        secret = 'secretpassword'
        psk = pykerio.structs.OptionalString({'enabled': True,
                                              'value': secret})
        network = pykerio.types.IpAddress('192.168.10.0')
        netmask = pykerio.types.IpAddress('255.255.255.0')
        dns1 = pykerio.types.IpAddress('192.168.10.1')
        dns2 = pykerio.types.IpAddress('192.168.10.1')
        wins1 = pykerio.types.IpAddress('192.168.10.1')
        wins2 = pykerio.types.IpAddress('192.168.10.1')
        route = pykerio.structs.VpnRoute({'id': pykerio.types.KId('Route 1'),
                                          'enabled': True,
                                          'description': 'Route LAN',
                                          'network': network,
                                          'mask': netmask})
        routes = pykerio.lists.VpnRouteList()
        routes.append(route)

        teststruct = pykerio.structs.VpnServerConfig({
            'kerioVpnEnabled': True,
            'kerioVpnCertificate': certificate,
            'port': 5090,
            'defaultRoute': False,
            'ipsecVpnEnabled': False,
            'mschapv2Enabled': False,
            'ipsecVpnCertificate': certificate,
            'cipherIke': secret,
            'cipherEsp': secret,
            'useCertificate': False,
            'psk': psk,
            'routes': routes,
            'network': network,
            'mask': netmask,
            'localDns': False,
            'primaryDns': dns1,
            'secondaryDns': dns2,
            'autodetectDomainSuffix': False,
            'domainSuffix': '',
            'localWins': False,
            'primaryWins': wins1,
            'secondaryWins': wins2})
        self.assertEquals(len(teststruct.keys()), 22)
        self.assertEquals(len(teststruct.values()), 22)

        self.assertEquals(teststruct['kerioVpnEnabled'], True)
        self.assertEquals(teststruct['psk'], psk)
        self.assertEquals(teststruct['primaryDns'], dns1)
        self.assertEquals(teststruct['secondaryDns'], dns2)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
