##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
#   Copyright: 2018-2023 Fabio Castelli
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

from pykerio.structs.base_struct import BaseStruct

from pykerio.enums.valid_type import ValidType

from pykerio.structs.date import Date
from pykerio.structs.time import Time


class ValidPeriod(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'validFromDate': Date,
                                   'validFromTime': Time,
                                   'validToDate': Date,
                                   'validToTime': Time,
                                   'validType': ValidType},
                            data=data)
