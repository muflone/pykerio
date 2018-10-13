##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

from ..json_serializable import JSONSerializable


class BaseList(list, JSONSerializable):
    def __init__(self, class_, *args, **kwargs):
        list.__init__(self, *args, **kwargs)
        JSONSerializable.__init__(self)
        self._class = class_

    def append(self, value):
        if not isinstance(value, self._class):
            #print('Type casting for list {TYPE} '
            #      'from {ACTUAL} to {REQUIRED}'.format(
            #          TYPE=self.__class__,
            #          ACTUAL=type(value),
            #          REQUIRED=self._class))
            value = self._class(value)
        assert(isinstance(value, self._class))
        list.append(self, value)

    def insert(self, index, value):
        assert(isinstance(value, self._class))
        list.insert(self, index, value)

    def dump(self):
        """JSON serializable representation"""
        return [value.dump() if isinstance(value, JSONSerializable) else value
                for value in self]

    def load(self, data):
        """Append a list of items"""
        for item in data:
            self.append(item)
