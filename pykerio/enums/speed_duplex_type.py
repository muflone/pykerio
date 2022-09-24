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


class SpeedDuplexType(BaseEnumeration):
    AUTO = 0
    HALF_10 = 1
    FULL_10 = 2
    HALF_100 = 3
    FULL_100 = 4
    FULL_1000 = 5

    VALUES = {
        'SpeedDuplexAuto': AUTO,
        'SpeedDuplexHalf10': HALF_10,
        'SpeedDuplexFull10': FULL_10,
        'SpeedDuplexHalf100': HALF_100,
        'SpeedDuplexFull100': FULL_100,
        'SpeedDuplexFull1000': FULL_1000
    }
