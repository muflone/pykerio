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
from pykerio.enums import (FailoverRoleType,
                           InterfaceEncapType,
                           InterfaceGroupType,
                           InterfaceModeType,
                           InterfaceStatusType,
                           InterfaceType,
                           MppeType,
                           RasType,
                           StoreStatus,
                           VpnType)


class TestCase_Interface(unittest.TestCase):
    def test_01_Interface(self):
        """
        Test Interface
        """
        localizablemessage = pykerio.structs.LocalizableMessage({
            'message': '',
            'positionalParameters': pykerio.lists.StringList(),
            'plurality': 0})
        details = pykerio.structs.DetailsConfig({
            'localizable': False,
            'fixedMessage': 'Port: LAN 3',
            'localizableMessage': localizablemessage})

        weight = pykerio.structs.OptionalLong({'enabled': True,
                                               'value': 1})
        interfaceparams = pykerio.structs.InterfaceConnectivityParameters({
            'failoverRole': FailoverRoleType.NONE,
            'onDemand': False,
            'loadBalancingWeight': weight})

        connecttime = pykerio.structs.OptionalEntity({
            'enabled': False,
            'id': pykerio.types.KId(''),
            'name': ''})
        certificate = pykerio.structs.IdReference({'id': pykerio.types.KId(''),
                                                   'name': '',
                                                   'invalid': False})
        rasconfig = pykerio.structs.RasConfig({
            'dead': False,
            'entryName': 'PPPoE101',
            'useOwnCredentials': False,
            'credentials': pykerio.structs.CredentialsConfig({
                'userName': '',
                'password': '',
                'passwordChanged': False}),
            'timeout': pykerio.structs.OptionalLong({'enabled': False,
                                                     'value': 0}),
            'connectTime': connecttime,
            'noConnectTime': connecttime,
            'bdScriptEnabled': False,
            'adScriptEnabled': False,
            'bhScriptEnabled': False,
            'ahScriptEnabled': False,
            'rasType': RasType.PPPoE,
            'pppoeIfaceId': '',
            'server': '',
            'papEnabled': False,
            'chapEnabled': False,
            'mschapEnabled': False,
            'mschapv2Enabled': False,
            'mppe': MppeType.MppeDisabled,
            'mppeStateful': False})

        vpnserver = pykerio.structs.VpnServerConfig({
            'kerioVpnEnabled': False,
            'kerioVpnCertificate': certificate,
            'port': 0,
            'defaultRoute': False,
            'ipsecVpnEnabled': False,
            'mschapv2Enabled': False,
            'ipsecVpnCertificate': certificate,
            'cipherIke': '',
            'cipherEsp': '',
            'useCertificate': False,
            'psk': pykerio.structs.OptionalString({'enabled': False,
                                                   'value': ''}),
            'routes': pykerio.lists.VpnRouteList(),
            'network': pykerio.types.IpAddress(''),
            'mask': pykerio.types.IpAddress(''),
            'localDns': False,
            'primaryDns': pykerio.types.IpAddress(''),
            'secondaryDns': pykerio.types.IpAddress(''),
            'autodetectDomainSuffix': False,
            'domainSuffix': '',
            'localWins': False,
            'primaryWins': pykerio.types.IpAddress(''),
            'secondaryWins': pykerio.types.IpAddress('')})

        vpntunnel = pykerio.structs.VpnTunnelConfig({
            'type': VpnType.VpnKerio,
            'peer': pykerio.structs.OptionalString({'enabled': False,
                                                    'value': ''}),
            'localRoutes': pykerio.lists.VpnRouteList(),
            'remoteRoutes': pykerio.lists.VpnRouteList(),
            'remoteFingerprint': '',
            'useRemoteAutomaticRoutes': False,
            'useRemoteCustomRoutes': False,
            'psk': pykerio.structs.OptionalString({'enabled': False,
                                                   'value': ''}),
            'certificate': certificate,
            'cipherIke': '',
            'cipherEsp': '',
            'localIdValue': '',
            'remoteIdValue': '',
            'useLocalAutomaticRoutes': False,
            'useLocalCustomRoutes': False})

        portslist = pykerio.lists.KIdList()
        portslist.append(pykerio.types.KId('4'))

        teststruct = pykerio.structs.Interface({
            'enabled': True,
            'type': InterfaceType.Ethernet,
            'status': StoreStatus.StoreStatusClean,
            'dhcpServerEnabled': False,
            'id': pykerio.types.KId('LanSwitch'),
            'group': InterfaceGroupType.Trusted,
            'name': 'LAN',
            'linkStatus': InterfaceStatusType.Up,
            'details': details,
            'mac': '00-90-0b-ff-ff-ff',
            'systemName': 'lan',
            'ip4Enabled': True,
            'mode': InterfaceModeType.InterfaceModeManual,
            'ip': pykerio.types.IpAddress('192.168.10.1'),
            'subnetMask': pykerio.types.IpAddress('255.255.255.0'),
            'secondaryAddresses': pykerio.lists.IpAddressMaskList(),
            'dnsAutodetected': True,
            'dnsServers': '',
            'gatewayAutodetected': True,
            'gateway': pykerio.types.IpAddress(''),
            'ip6Enabled': True,
            'ip6Mode': InterfaceModeType.InterfaceModeAutomatic,
            'ip6Addresses': pykerio.lists.Ip6AddressMaskList(),
            'linkIp6Address': pykerio.types.Ip6Address(
                'fe80::290:fff:fff:fff'),
            'ip6Gateway': pykerio.types.IpAddress(''),
            'routedIp6PrefixAutodetected': True,
            'routedIp6Prefix': '',
            'connectivityParameters': interfaceparams,
            'encap': InterfaceEncapType.InterfaceEncapNative,
            'mtuOverride': pykerio.structs.OptionalLong({'enabled': False,
                                                         'value': 0}),
            'macOverride': pykerio.structs.OptionalString({'enabled': False,
                                                           'value': ''}),
            'ras': rasconfig,
            'server': vpnserver,
            'tunnel': vpntunnel,
            'flags': pykerio.structs.InterfaceFlags({'deletable': False,
                                                     'dialable': False,
                                                     'hangable': False,
                                                     'virtualSwitch': True,
                                                     'wifi': False,
                                                     'vlan': False}),
            'ports': portslist,
            'stp': True,
            'vlanId': 0,
            'ssidId': pykerio.types.KId('')
            })
        self.assertEqual(len(teststruct.keys()), 39)
        self.assertEqual(len(teststruct.values()), 39)

        self.assertEqual(teststruct['connectivityParameters'], interfaceparams)
        self.assertEqual(teststruct['ras'], rasconfig)
        self.assertEqual(teststruct['server'], vpnserver)
        self.assertEqual(teststruct['tunnel'], vpntunnel)
        self.assertEqual(teststruct['ports'], portslist)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
