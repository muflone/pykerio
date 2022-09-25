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

from pykerio.enums.base_enumeration import BaseEnumeration


class FacilityUnit(BaseEnumeration):
    FacilityKernel = 0
    FacilityUserLevel = 1
    FacilityMailSystem = 2
    FacilitySystemDaemons = 3
    FacilitySecurity1 = 4
    FacilityInternal = 5
    FacilityLinePrinter = 6
    FacilityNetworkNews = 7
    FacilityUucpSubsystem = 8
    FacilityClockDaemon1 = 9
    FacilitySecurity2 = 10
    FacilityFtpDaemon = 11
    FacilityNtpSubsystem = 12
    FacilityLogAudit = 13
    FacilityLogAlert = 14
    FacilityClockDaemon2 = 15
    FacilityLocal0 = 16
    FacilityLocal1 = 17
    FacilityLocal2 = 18
    FacilityLocal3 = 19
    FacilityLocal4 = 20
    FacilityLocal5 = 21
    FacilityLocal6 = 22
    FacilityLocal7 = 23
