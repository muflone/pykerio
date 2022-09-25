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

from pykerio.enums.logical_operator import LogicalOperator
from pykerio.lists.sort_order_list import SortOrderList
from pykerio.lists.string_list import StringList
from pykerio.lists.sub_condition_list import SubConditionList
from pykerio.structs.base_struct import BaseStruct


class SearchQuery(BaseStruct):
    """
    General Query for Searching

    Query substitution (quicksearch):

    SearchQuery doesn't support complex queries, only queries
    with all AND operators (or all OR operators) are supported.
    Combination of AND and OR is not allowed. This limitation is for special
    cases solved by using substitution of complicated query-part by simple
    condition.

    Only the quicksearch is currently implemented and only in "Users::get()"
    method.
    Behavior of quicksearch in Users::get():
    QUICKSEARCH    = "x"   is equal to:   (loginName    = "x")
                                          OR (fullName    = "x")
    QUICKSEARCH LIKE "x*"  is equal to:   (loginName LIKE "x*")
                                          OR (fullName LIKE "x*")
    QUICKSEARCH   <> "x"   is equal to:   (loginName   <> "x")
                                          AND (fullName   <> "x")
    """
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'fields': StringList,
                                   'conditions': SubConditionList,
                                   'combining': LogicalOperator,
                                   'start': int,
                                   'limit': int,
                                   'orderBy': SortOrderList},
                            data=data)
