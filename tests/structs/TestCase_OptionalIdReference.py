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

import unittest

import pykerio


class TestCase_OptionalIdReference(unittest.TestCase):
    def test_01_OptionalIdReference(self):
        """
        Test OptionalIdReference
        """
        enabled = True
        kid = pykerio.types.KId('user1')
        name = 'User 1'
        idref = pykerio.structs.IdReference({'id': kid,
                                             'name': name,
                                             'invalid': False})
        teststruct = pykerio.structs.OptionalIdReference({'enabled': enabled,
                                                          'value': idref})
        self.assertEquals(len(teststruct.keys()), 2)
        self.assertEquals(len(teststruct.values()), 2)

        self.assertEquals(teststruct['enabled'], enabled)
        self.assertEquals(teststruct['value'], idref)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
