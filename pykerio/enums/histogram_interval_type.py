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


class HistogramIntervalType(BaseEnumeration):
    INTERVAL_5M = 0
    INTERVAL_20S = 1
    INTERVAL_30M = 2
    INTERVAL_2H = 3

    VALUES = {
        'HistogramInterval5m': INTERVAL_5M,
        'HistogramInterval20s': INTERVAL_20S,
        'HistogramInterval30m': INTERVAL_30M,
        'HistogramInterval2h': INTERVAL_2H
    }
