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
from pykerio.json_serializable import JSONSerializable


class BaseStruct(dict, JSONSerializable):
    def __init__(self, types: dict, data: dict):
        # Check members type
        new_data = {}
        for key in types:
            assert key in data
            item = data[key]
            if type(item) is not types[key]:
                # print('Type casting for argument {KEY} '
                #       'from {ACTUAL} to {REQUIRED}'.format(
                #           KEY=key,
                #           ACTUAL=type(item),
                #           REQUIRED=types[key]))
                if issubclass(types[key], BaseEnumeration):
                    item = types[key].from_name(data[key])
                else:
                    item = types[key](data[key])
            if type(item) is not types[key]:
                print('Type clashing for argument {KEY}'.format(KEY=key))
                print('  required type: {REQUIRED}'.format(
                    REQUIRED=types[key]))
                print('  actual type: {ACTUAL}'.format(ACTUAL=type(item)))
                assert type(item) is types[key]
            else:
                new_data[key] = item
        # Limit members to only those listed in keys
        dict.__init__(self,
                      dict([(key, value) for key, value in new_data.items()
                            if key in types.keys()]))
        JSONSerializable.__init__(self)

    def dump(self):
        """JSON serializable representation"""
        return dict((key, value.dump() if isinstance(value, JSONSerializable)
                     else value) for (key, value) in self.items())
