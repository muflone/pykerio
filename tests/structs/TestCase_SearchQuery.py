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


class TestCase_SearchQuery(unittest.TestCase):
    def test_01_SearchQuery(self):
        """
        Test SearchQuery
        """
        fields = pykerio.lists.StringList()
        fields.append('interface')
        fields.append('type')

        comparator = pykerio.enums.CompareOperator('Like')
        condition = pykerio.structs.SubCondition({'fieldName': 'name',
                                                  'comparator': comparator,
                                                  'value': 'LAN'})
        conditions = pykerio.lists.SubConditionList()
        conditions.append(condition)

        comparator = pykerio.enums.CompareOperator('Eq')
        condition = pykerio.structs.SubCondition({'fieldName': 'name',
                                                  'comparator': comparator,
                                                  'value': 'VPN'})
        conditions.append(condition)

        combining = pykerio.enums.LogicalOperator('Or')

        sort_direction = pykerio.enums.SortDirection(name='Asc')
        order = pykerio.structs.SortOrder({'columnName': 'name',
                                           'direction': sort_direction,
                                           'caseSensitive': False})
        orderbylist = pykerio.lists.SortOrderList(order)

        teststruct = pykerio.structs.SearchQuery({'fields': fields,
                                                  'conditions': conditions,
                                                  'combining': combining,
                                                  'start': 0,
                                                  'limit': pykerio.constants.UNLIMITED,
                                                  'orderBy': orderbylist})
        self.assertEquals(len(teststruct.keys()), 6)
        self.assertEquals(len(teststruct.values()), 6)

        self.assertEquals(teststruct['fields'], fields)
        self.assertEquals(teststruct['conditions'], conditions)
        self.assertEquals(teststruct['combining'], combining)
        self.assertEquals(teststruct['start'], 0)
        self.assertEquals(teststruct['limit'], pykerio.constants.UNLIMITED)
        self.assertEquals(teststruct['orderBy'], orderbylist)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
