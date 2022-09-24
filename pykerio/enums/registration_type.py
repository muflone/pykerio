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

from .base_enumeration import BaseEnumeration


class RegistrationType(BaseEnumeration):
    NO_REGISTRATION = 0
    TRIAL_REGISTERED = 1
    TRIAL_EXPIRED = 2
    REGISTERED = 3

    VALUES = {
        'rsNoRegistration': NO_REGISTRATION,
        'rsTrialRegistered': TRIAL_REGISTERED,
        'rsTrialExpired': TRIAL_EXPIRED,
        'rsProductRegistered': REGISTERED
    }
