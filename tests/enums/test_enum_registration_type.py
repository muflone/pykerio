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


class TestCase_RegistrationType(unittest.TestCase):
    def test_00_RegistrationType_rsNoRegistration(self):
        """
        Test RegistrationType with rsNoRegistration
        """
        value = pykerio.enums.RegistrationType(name='rsNoRegistration')
        self.assertEqual(value.dump(), 'rsNoRegistration')
        self.assertEqual(value.get_name(), 'rsNoRegistration')
        self.assertEqual(value.get_value(), 0)

    def test_01_RegistrationType_rsTrialRegistered(self):
        """
        Test RegistrationType with rsTrialRegistered
        """
        value = pykerio.enums.RegistrationType(name='rsTrialRegistered')
        self.assertEqual(value.dump(), 'rsTrialRegistered')
        self.assertEqual(value.get_name(), 'rsTrialRegistered')
        self.assertEqual(value.get_value(), 1)

    def test_02_RegistrationType_rsTrialExpired(self):
        """
        Test RegistrationType with rsTrialExpired
        """
        value = pykerio.enums.RegistrationType(name='rsTrialExpired')
        self.assertEqual(value.dump(), 'rsTrialExpired')
        self.assertEqual(value.get_name(), 'rsTrialExpired')
        self.assertEqual(value.get_value(), 2)

    def test_03_RegistrationType_rsProductRegistered(self):
        """
        Test RegistrationType with rsProductRegistered
        """
        value = pykerio.enums.RegistrationType(name='rsProductRegistered')
        self.assertEqual(value.dump(), 'rsProductRegistered')
        self.assertEqual(value.get_name(), 'rsProductRegistered')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_RegistrationType_FAIL(self):
        """
        Test RegistrationType with FAIL
        """
        value = pykerio.enums.RegistrationType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
