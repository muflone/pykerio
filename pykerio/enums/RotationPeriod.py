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


class RotationPeriod(BaseEnumeration):
    NEVER = 0
    HOURLY = 1
    DAILY = 2
    WEEKLY = 3
    MONTHLY = 4

    VALUES = {
        'RotateNever': NEVER,
        'RotateHourly': HOURLY,
        'RotateDaily': DAILY,
        'RotateWeekly': WEEKLY,
        'RotateMonthly': MONTHLY
    }
