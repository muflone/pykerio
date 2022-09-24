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


class PortComparator(BaseEnumeration):
    ANY = 0
    EQUAL = 1
    LESS_THAN = 2
    GREATER_THAN = 3
    RANGE = 4
    LIST = 5

    VALUES = {
        'Any': ANY,
        'Equal': EQUAL,
        'LessThan': LESS_THAN,
        'GreaterThan': GREATER_THAN,
        'Range': RANGE,
        'List': LIST
    }
