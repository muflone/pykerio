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

from .base_enumeration import BaseEnumeration


class DhcpOptionType(BaseEnumeration):
    BOOL = 0
    INT8 = 1
    INT16 = 2
    INT32 = 3
    IP_ADDR = 4
    STRING = 5
    HEX = 6
    TIME_SIGNED = 7
    TIME_UNSIGNED = 8
    INT8_LIST = 9
    INT16_LIST = 10
    INT32_LIST = 11
    IP_ADDR_LIST = 12
    IP_PAIR_LIST = 13
    IP_MASK_LIST = 14
    IP_MASK_IP_LIST = 15

    VALUES = {
        'DhcpBool': BOOL,
        'DhcpInt8': INT8,
        'DhcpInt16': INT16,
        'DhcpInt32': INT32,
        'DhcpIpAddr': IP_ADDR,
        'DhcpString': STRING,
        'DhcpHex': HEX,
        'DhcpTimeSigned': TIME_SIGNED,
        'DhcpTimeUnsigned': TIME_UNSIGNED,
        'DhcpInt8List': INT8_LIST,
        'DhcpInt16List': INT16_LIST,
        'DhcpInt32List': INT32_LIST,
        'DhcpIpAddrList': IP_ADDR_LIST,
        'DhcpIpPairList': IP_PAIR_LIST,
        'DhcpIpMaskList': IP_MASK_LIST,
        'DhcpIpMaskIpList': IP_MASK_IP_LIST
    }
