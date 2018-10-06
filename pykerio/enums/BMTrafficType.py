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


class BMTrafficType(BaseEnumeration):
    VALUES = {'BMTrafficEmail': 0,
              'BMTrafficFtp': 1,
              'BMTrafficInstantMessaging': 2,
              'BMTrafficMultimedia': 3,
              'BMTrafficP2p': 4,
              'BMTrafficRemoteAccess': 5,
              'BMTrafficSip': 6,
              'BMTrafficVpn': 7,
              'BMTrafficWeb': 8
             }
