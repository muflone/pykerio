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


class WifiEncryptionType(BaseEnumeration):
    DISABLED = 0
    WPA_PSK = 1
    WPA_ENT = 2
    WPA2_PSK = 3
    WPA2_ENT = 4

    VALUES = {
        'WifiEncryptionDisabled': DISABLED,
        'WifiEncryptionWpaPsk': WPA_PSK,
        'WifiEncryptionWpaEnt': WPA_ENT,
        'WifiEncryptionWpa2Psk': WPA2_PSK,
        'WifiEncryptionWpa2Ent': WPA2_ENT
    }
