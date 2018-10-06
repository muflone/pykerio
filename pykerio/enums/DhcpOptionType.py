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

from . import BaseEnumeration


class DhcpOptionType(BaseEnumeration):
    VALUES = {'DhcpBool': 0,
              'DhcpInt8': 1,
              'DhcpInt16': 2,
              'DhcpInt32': 3,
              'DhcpIpAddr': 4,
              'DhcpString': 5,
              'DhcpHex': 6,
              'DhcpTimeSigned': 7,
              'DhcpTimeUnsigned': 8,
              'DhcpInt8List': 9,
              'DhcpInt16List': 10,
              'DhcpInt32List': 11,
              'DhcpIpAddrList': 12,
              'DhcpIpPairList': 13,
              'DhcpIpMaskList': 14,
              'DhcpIpMaskIpList': 15
             }
