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


class InterfaceStatusType(BaseEnumeration):
    UP = 0
    DOWN = 1
    CONNECTING = 2
    DISCONNECTING = 3
    CABLE_DISCONNECTED = 4
    ERROR = 5
    BACKUP = 6

    VALUES = {
        'Up': UP,
        'Down': DOWN,
        'Connecting': CONNECTING,
        'Disconnecting': DISCONNECTING,
        'CableDisconnected': CABLE_DISCONNECTED,
        'Error': ERROR,
        'Backup': BACKUP
    }
