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

from ..json_serializable import JSONSerializable


class BaseEnumeration(JSONSerializable):
    VALUES = {}

    def __init__(self, name):
        JSONSerializable.__init__(self)
        assert name in self.VALUES
        self._name = name

    def dump(self):
        """JSON serializable representation"""
        return self.get_name()

    def get_name(self):
        """Return the enumeration name"""
        return self._name

    def get_value(self):
        """Return the enumeration value"""
        return self.VALUES[self._name]
