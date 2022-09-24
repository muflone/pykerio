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

from . import BaseEnumeration


class BMTrafficType(BaseEnumeration):
    EMAIL = 0
    FTP = 1
    INSTANT_MESSAGING = 2
    MULTIMEDIA = 3
    P2P = 4
    REMOTE_ACCESS = 5
    SIP = 6
    VPN = 7
    WEB = 8

    VALUES = {
        'BMTrafficEmail': EMAIL,
        'BMTrafficFtp': FTP,
        'BMTrafficInstantMessaging': INSTANT_MESSAGING,
        'BMTrafficMultimedia': MULTIMEDIA,
        'BMTrafficP2p': P2P,
        'BMTrafficRemoteAccess': REMOTE_ACCESS,
        'BMTrafficSip': SIP,
        'BMTrafficVpn': VPN,
        'BMTrafficWeb': WEB
    }
