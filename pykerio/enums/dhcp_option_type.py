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

from pykerio.enums.base_enumeration import BaseEnumeration


class DhcpOptionType(BaseEnumeration):
    DhcpBool = 0
    DhcpInt8 = 1
    DhcpInt16 = 2
    DhcpInt32 = 3
    DhcpIpAddr = 4
    DhcpString = 5
    DhcpHex = 6
    DhcpTimeSigned = 7
    DhcpTimeUnsigned = 8
    DhcpInt8List = 9
    DhcpInt16List = 10
    DhcpInt32List = 11
    DhcpIpAddrList = 12
    DhcpIpPairList = 13
    DhcpIpMaskList = 14
    DhcpIpMaskIpList = 15
