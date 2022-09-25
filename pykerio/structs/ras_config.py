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

from pykerio.enums.ras_type import RasType
from pykerio.enums.mppe_type import MppeType
from pykerio.structs.base_struct import BaseStruct
from pykerio.structs.credentials_config import CredentialsConfig
from pykerio.structs.optional_entity import OptionalEntity
from pykerio.structs.optional_long import OptionalLong


class RasConfig(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'dead': bool,
                                   'entryName': str,
                                   'useOwnCredentials': bool,
                                   'credentials': CredentialsConfig,
                                   'timeout': OptionalLong,
                                   'connectTime': OptionalEntity,
                                   'noConnectTime': OptionalEntity,
                                   'bdScriptEnabled': bool,
                                   'adScriptEnabled': bool,
                                   'bhScriptEnabled': bool,
                                   'ahScriptEnabled': bool,
                                   'rasType': RasType,
                                   'pppoeIfaceId': str,
                                   'server': str,
                                   'papEnabled': bool,
                                   'chapEnabled': bool,
                                   'mschapEnabled': bool,
                                   'mschapv2Enabled': bool,
                                   'mppe': MppeType,
                                   'mppeStateful': bool},
                            data=data)
