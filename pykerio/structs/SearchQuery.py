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

from . import BaseStruct

from ..enums.LogicalOperator import LogicalOperator

from ..lists.SortOrderList import SortOrderList
from ..lists.StringList import StringList
from ..lists.SubConditionList import SubConditionList


class SearchQuery(BaseStruct):
    """
    General Query for Searching

    Query substitution (quicksearch):

    SearchQuery doesn't support complex queries, only queries
    with all AND operators (or all OR operators) are supported.
    Combination of AND and OR is not allowed. This limitation is for special
    cases solved by using substitution of complicated query-part by simple
    condition.

    Only the quicksearch is currently implemented and only in "Users::get()" method.
    Behavior of quicksearch in Users::get():
    QUICKSEARCH    = "x"   is equal to:   (loginName    = "x")  OR (fullName    = "x")
    QUICKSEARCH LIKE "x*"  is equal to:   (loginName LIKE "x*") OR (fullName LIKE "x*")
    QUICKSEARCH   <> "x"   is equal to:   (loginName   <> "x") AND (fullName   <> "x")
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
