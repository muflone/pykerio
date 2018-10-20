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

from ..enums.PortAssignmentType import PortAssignmentType
from ..enums.PortType import PortType
from ..enums.SpeedDuplexType import SpeedDuplexType

from ..lists.SpeedDuplexMayNotWorkList import SpeedDuplexMayNotWorkList

from ..structs.OptionalString import OptionalString

from ..types.KId import KId


class PortConfig(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'id': KId,
                                   'type': PortType,
                                   'name': str,
                                   'assignment': PortAssignmentType,
                                   'vlans': OptionalString,
                                   'speedDuplex': SpeedDuplexType,
                                   'speedDuplexMayNotWork':
                                       SpeedDuplexMayNotWorkList},
                            data=data)
