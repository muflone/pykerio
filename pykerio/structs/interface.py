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

from pykerio.enums.interface_encap_type import InterfaceEncapType
from pykerio.enums.interface_group_type import InterfaceGroupType
from pykerio.enums.interface_mode_type import InterfaceModeType
from pykerio.enums.interface_status_type import InterfaceStatusType
from pykerio.enums.interface_type import InterfaceType
from pykerio.enums.store_status import StoreStatus
from pykerio.lists.ip_address_mask_list import IpAddressMaskList
from pykerio.lists.ip6_address_mask_list import Ip6AddressMaskList
from pykerio.lists.kid_list import KIdList
from pykerio.structs.base_struct import BaseStruct
from pykerio.structs.details_config import DetailsConfig
from pykerio.structs.interface_connectivity_parameters import (
       InterfaceConnectivityParameters)
from pykerio.structs.interface_flags import InterfaceFlags
from pykerio.structs.optional_long import OptionalLong
from pykerio.structs.optional_string import OptionalString
from pykerio.structs.ras_config import RasConfig
from pykerio.structs.vpn_server_config import VpnServerConfig
from pykerio.structs.vpn_tunnel_config import VpnTunnelConfig
from pykerio.types.ip_address import IpAddress
from pykerio.types.ip6_address import Ip6Address
from pykerio.types.kid import KId


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
                                   'connectivityParameters':
                                   InterfaceConnectivityParameters,
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
