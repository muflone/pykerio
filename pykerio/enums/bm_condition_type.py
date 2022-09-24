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


class BMConditionType(BaseEnumeration):
    TRAFFIC_TYPE = 0
    QUOTA = 1
    LARGE_DATA = 2
    TRAFFIC_RULE = 3
    CONTENT_RULE = 4
    SERVICE = 5
    DSCP = 6
    USERS = 7
    INVALID = 8
    RULE_TYPE = 9
    GUESTS = 10
    APPLICATION = 11

    VALUES = {
        'BMConditionTrafficType': TRAFFIC_TYPE,
        'BMConditionQuota': QUOTA,
        'BMConditionLargeData': LARGE_DATA,
        'BMConditionTrafficRule': TRAFFIC_RULE,
        'BMConditionContentRule': CONTENT_RULE,
        'BMConditionService': SERVICE,
        'BMConditionDscp': DSCP,
        'BMConditionUsers': USERS,
        'BMConditionInvalid': INVALID,
        'BMContentRuleType': RULE_TYPE,
        'BMConditionGuests': GUESTS,
        'BMConditionApplication': APPLICATION
    }
