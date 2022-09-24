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


class ByteUnits(BaseEnumeration):
    BYTES = 0
    KILO_BYTES = 1
    MEGA_BYTES = 2
    GIGA_BYTES = 3
    TERA_BYTES = 4
    PETA_BYTES = 5

    VALUES = {
        'Bytes': BYTES,
        'KiloBytes': KILO_BYTES,
        'MegaBytes': MEGA_BYTES,
        'GigaBytes': GIGA_BYTES,
        'TeraBytes': TERA_BYTES,
        'PetaBytes': PETA_BYTES
    }
