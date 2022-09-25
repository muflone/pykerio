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

from pykerio.enums.vpn_type import VpnType
from pykerio.lists.vpn_route_list import VpnRouteList
from pykerio.structs.base_struct import BaseStruct
from pykerio.structs.id_reference import IdReference
from pykerio.structs.optional_string import OptionalString


class VpnTunnelConfig(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'type': VpnType,
                                   'peer': OptionalString,
                                   'localRoutes': VpnRouteList,
                                   'remoteRoutes': VpnRouteList,
                                   'remoteFingerprint': str,
                                   'useRemoteAutomaticRoutes': bool,
                                   'useRemoteCustomRoutes': bool,
                                   'psk': OptionalString,
                                   'certificate': IdReference,
                                   'cipherIke': str,
                                   'cipherEsp': str,
                                   'localIdValue': str,
                                   'remoteIdValue': str,
                                   'useLocalAutomaticRoutes': bool,
                                   'useLocalCustomRoutes': bool},
                            data=data)
