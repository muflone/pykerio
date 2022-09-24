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


class Entity(BaseEnumeration):
    USER = 0
    ALIAS = 1
    GROUP = 2
    MAILING_LIST = 3
    RESOURCE = 4
    TIME_RANGE = 5
    TIME_RANGE_GROUP = 6
    IP_ADDRESS = 7
    IP_ADDRESS_GROUP = 8
    SERVICE = 9
    DOMAIN = 10

    VALUES = {
        'EntityUser': USER,
        'EntityAlias': ALIAS,
        'EntityGroup': GROUP,
        'EntityMailingList': MAILING_LIST,
        'EntityResource': RESOURCE,
        'EntityTimeRange': TIME_RANGE,
        'EntityTimeRangeGroup': TIME_RANGE_GROUP,
        'EntityIpAddress': IP_ADDRESS,
        'EntityIpAddressGroup': IP_ADDRESS_GROUP,
        'EntityService': SERVICE,
        'EntityDomain': DOMAIN
    }
