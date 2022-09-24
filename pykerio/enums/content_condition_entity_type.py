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


class ContentConditionEntityType(BaseEnumeration):
    APPLICATION = 0
    FILE_NAME = 1
    FILE_GROUP = 2
    URL = 3
    URL_GROUP = 4

    VALUES = {
        'ContentConditionEntityApplication': APPLICATION,
        'ContentConditionEntityFileName': FILE_NAME,
        'ContentConditionEntityFileGroup': FILE_GROUP,
        'ContentConditionEntityUrl': URL,
        'ContentConditionEntityUrlGroup': URL_GROUP
    }
