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

from pykerio.enums import RegistrationType


class TestCase_RegistrationType(unittest.TestCase):
    def test_00_rsNoRegistration(self):
        """
        Test RegistrationType with rsNoRegistration
        """
        value = RegistrationType.rsNoRegistration
        self.assertEqual(value.dump(), 'rsNoRegistration')
        self.assertEqual(value.name, 'rsNoRegistration')
        self.assertEqual(value.value, 0)

    def test_01_rsTrialRegistered(self):
        """
        Test RegistrationType with rsTrialRegistered
        """
        value = RegistrationType.rsTrialRegistered
        self.assertEqual(value.dump(), 'rsTrialRegistered')
        self.assertEqual(value.name, 'rsTrialRegistered')
        self.assertEqual(value.value, 1)

    def test_02_rsTrialExpired(self):
        """
        Test RegistrationType with rsTrialExpired
        """
        value = RegistrationType.rsTrialExpired
        self.assertEqual(value.dump(), 'rsTrialExpired')
        self.assertEqual(value.name, 'rsTrialExpired')
        self.assertEqual(value.value, 2)

    def test_03_rsProductRegistered(self):
        """
        Test RegistrationType with rsProductRegistered
        """
        value = RegistrationType.rsProductRegistered
        self.assertEqual(value.dump(), 'rsProductRegistered')
        self.assertEqual(value.name, 'rsProductRegistered')
        self.assertEqual(value.value, 3)
