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

from pykerio.enums.base_enumeration import BaseEnumeration


class Entity(BaseEnumeration):
    EntityUser = 0
    EntityAlias = 1
    EntityGroup = 2
    EntityMailingList = 3
    EntityResource = 4
    EntityTimeRange = 5
    EntityTimeRangeGroup = 6
    EntityIpAddress = 7
    EntityIpAddressGroup = 8
    EntityService = 9
    EntityDomain = 10
