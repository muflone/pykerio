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

from . import BaseEnumeration


class FacilityUnit(BaseEnumeration):
    KERNEL = 0
    USER_LEVEL = 1
    MAIL_SYSTEM = 2
    SYSTEM_DAEMONS = 3
    SECURITY1 = 4
    INTERNAL = 5
    LINE_PRINTER = 6
    NETWORK_NEWS = 7
    UUCP_SUBSYSTEM = 8
    CLOCK_DAEMON1 = 9
    SECURITY2 = 10
    FTP_DAEMON = 11
    NTP_SUBSYSTEM = 12
    LOG_AUDIT = 13
    LOG_ALERT = 14
    CLOCK_DAEMON2 = 15
    LOCAL0 = 16
    LOCAL1 = 17
    LOCAL2 = 18
    LOCAL3 = 19
    LOCAL4 = 20
    LOCAL5 = 21
    LOCAL6 = 22
    LOCAL7 = 23

    VALUES = {
        'FacilityKernel': KERNEL,
        'FacilityUserLevel': USER_LEVEL,
        'FacilityMailSystem': MAIL_SYSTEM,
        'FacilitySystemDaemons': SYSTEM_DAEMONS,
        'FacilitySecurity1': SECURITY1,
        'FacilityInternal': INTERNAL,
        'FacilityLinePrinter': LINE_PRINTER,
        'FacilityNetworkNews': NETWORK_NEWS,
        'FacilityUucpSubsystem': UUCP_SUBSYSTEM,
        'FacilityClockDaemon1': CLOCK_DAEMON1,
        'FacilitySecurity2': SECURITY2,
        'FacilityFtpDaemon': FTP_DAEMON,
        'FacilityNtpSubsystem': NTP_SUBSYSTEM,
        'FacilityLogAudit': LOG_AUDIT,
        'FacilityLogAlert': LOG_ALERT,
        'FacilityClockDaemon2': CLOCK_DAEMON2,
        'FacilityLocal0': LOCAL0,
        'FacilityLocal1': LOCAL1,
        'FacilityLocal2': LOCAL2,
        'FacilityLocal3': LOCAL3,
        'FacilityLocal4': LOCAL4,
        'FacilityLocal5': LOCAL5,
        'FacilityLocal6': LOCAL6,
        'FacilityLocal7': LOCAL7
    }
