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


class TestCase_Collision(unittest.TestCase):
    def test_01_Collision(self):
        """
        Test Collision
        """
        rule1 = pykerio.types.KId('rule1')
        idref1 = pykerio.structs.IdReference({'id': rule1,
                                              'name': 'Rule 1',
                                              'invalid': False})
        rule2 = pykerio.types.KId('rule2')
        idref2 = pykerio.structs.IdReference({'id': rule2,
                                              'name': 'Rule 2',
                                              'invalid': False})
        teststruct = pykerio.structs.Collision({
            'rule': idref1,
            'overlappedRule': idref2})
        self.assertEquals(len(teststruct.keys()), 2)
        self.assertEquals(len(teststruct.values()), 2)

        self.assertEquals(teststruct['rule'], idref1)
        self.assertEquals(teststruct['overlappedRule'], idref2)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
