##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@vbsimple.net>
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
from ..primitives import StringList

class LocalizableMessageParameters(JSONSerializable):
    """
    Message can contain replacement marks:
    { "User %1 cannot be deleted.", ["jsmith"], 1 }.
    This is the parameters structure.
    """
    def __init__(self, data: dict):
        self.positionalParameters = StringList(data['positionalParameters'])
        self.plurality = data['plurality']

    def dump(self):
        """JSON serializable representation"""
        return {'positionalParameters': self.positionalParameters,
                'plurality': self.plurality
               }