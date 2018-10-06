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


class BaseStruct(dict, JSONSerializable):
    def __init__(self, types: dict, data: dict):
        # Check members type
        assert(not [key for key, value in types.items()
               if type(data[key]) is not types[key]])
        # Limit members to only those listed in keys
        dict.__init__(self, dict([(key, value) for key, value in data.items()
                                  if key in types.keys()]))
        JSONSerializable.__init__(self)

    def dump(self):
        """JSON serializable representation"""
        return str(self)
