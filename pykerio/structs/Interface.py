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

from . import BaseStruct

from ..enums.StoreStatus import StoreStatus

from ..enums.InterfaceEncapType import InterfaceEncapType
from ..enums.InterfaceGroupType import InterfaceGroupType
from ..enums.InterfaceModeType import InterfaceModeType
from ..enums.InterfaceStatusType import InterfaceStatusType
from ..enums.InterfaceType import InterfaceType

from ..lists.IpAddressMaskList import IpAddressMaskList
from ..lists.Ip6AddressMaskList import Ip6AddressMaskList
from ..lists.KIdList import KIdList

from ..structs.DetailsConfig import DetailsConfig
from ..structs.InterfaceConnectivityParameters import InterfaceConnectivityParameters
from ..structs.InterfaceFlags import InterfaceFlags
from ..structs.OptionalLong import OptionalLong
from ..structs.OptionalString import OptionalString
from ..structs.RasConfig import RasConfig
from ..structs.VpnServerConfig import VpnServerConfig
from ..structs.VpnTunnelConfig import VpnTunnelConfig

from ..types.IpAddress import IpAddress
from ..types.Ip6Address import Ip6Address
from ..types.KId import KId


class Interface(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'enabled': bool,
                                   'type': InterfaceType,
                                   'status': StoreStatus,
                                   'dhcpServerEnabled': bool,
                                   'id': KId,
                                   'group': InterfaceGroupType,
                                   'name': str,
                                   'linkStatus': InterfaceStatusType,
                                   'details': DetailsConfig,
                                   'mac': str,
                                   'systemName': str,
                                   'ip4Enabled': bool,
                                   'mode': InterfaceModeType,
                                   'ip': IpAddress,
                                   'subnetMask': IpAddress,
                                   'secondaryAddresses': IpAddressMaskList,
                                   'dnsAutodetected': bool,
                                   'dnsServers': str,
                                   'gatewayAutodetected': bool,
                                   'gateway': IpAddress,
                                   'ip6Enabled': bool,
                                   'ip6Mode': InterfaceModeType,
                                   'ip6Addresses': Ip6AddressMaskList,
                                   'linkIp6Address': Ip6Address,
                                   'ip6Gateway': IpAddress,
                                   'routedIp6PrefixAutodetected': bool,
                                   'routedIp6Prefix': str,
                                   'connectivityParameters': InterfaceConnectivityParameters,
                                   'encap': InterfaceEncapType,
                                   'mtuOverride': OptionalLong,
                                   'macOverride': OptionalString,
                                   'ras': RasConfig,
                                   'server': VpnServerConfig,
                                   'tunnel': VpnTunnelConfig,
                                   'flags': InterfaceFlags,
                                   'ports': KIdList,
                                   'stp': bool,
                                   'vlanId': int,
                                   'ssidId': KId},
                            data=data)
