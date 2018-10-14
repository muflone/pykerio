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

import unittest

import pykerio


class TestCase_OptionalEntity(unittest.TestCase):
    def test_01_OptionalEntity(self):
        """
        Test OptionalEntity
        """
        enabled = True
        kid = pykerio.types.KId('Object name')
        name = 'Object name'
        teststruct = pykerio.structs.OptionalEntity({'enabled': enabled,
                                                     'id': kid,
                                                     'name': name})
        self.assertEquals(len(teststruct.keys()), 3)
        self.assertEquals(len(teststruct.values()), 3)

        self.assertEquals(teststruct['enabled'], enabled)
        self.assertEquals(teststruct['id'], kid)
        self.assertEquals(teststruct['name'], name)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
