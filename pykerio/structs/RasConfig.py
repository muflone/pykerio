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

from ..enums.RasType import RasType
from ..enums.MppeType import MppeType

from ..structs.CredentialsConfig import CredentialsConfig
from ..structs.OptionalEntity import OptionalEntity
from ..structs.OptionalLong import OptionalLong


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
