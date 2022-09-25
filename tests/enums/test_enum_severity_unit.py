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


class TestCase_SeverityUnit(unittest.TestCase):
    def test_00_SeverityEmergency(self):
        """
        Test SeverityUnit with SeverityEmergency
        """
        value = pykerio.enums.SeverityUnit(name='SeverityEmergency')
        self.assertEqual(value.dump(), 'SeverityEmergency')
        self.assertEqual(value.get_name(), 'SeverityEmergency')
        self.assertEqual(value.get_value(), 0)

    def test_01_SeverityAlert(self):
        """
        Test SeverityUnit with SeverityAlert
        """
        value = pykerio.enums.SeverityUnit(name='SeverityAlert')
        self.assertEqual(value.dump(), 'SeverityAlert')
        self.assertEqual(value.get_name(), 'SeverityAlert')
        self.assertEqual(value.get_value(), 1)

    def test_02_SeverityCritical(self):
        """
        Test SeverityUnit with SeverityCritical
        """
        value = pykerio.enums.SeverityUnit(name='SeverityCritical')
        self.assertEqual(value.dump(), 'SeverityCritical')
        self.assertEqual(value.get_name(), 'SeverityCritical')
        self.assertEqual(value.get_value(), 2)

    def test_03_SeverityError(self):
        """
        Test SeverityUnit with SeverityError
        """
        value = pykerio.enums.SeverityUnit(name='SeverityError')
        self.assertEqual(value.dump(), 'SeverityError')
        self.assertEqual(value.get_name(), 'SeverityError')
        self.assertEqual(value.get_value(), 3)

    def test_04_SeverityWarning(self):
        """
        Test SeverityUnit with SeverityWarning
        """
        value = pykerio.enums.SeverityUnit(name='SeverityWarning')
        self.assertEqual(value.dump(), 'SeverityWarning')
        self.assertEqual(value.get_name(), 'SeverityWarning')
        self.assertEqual(value.get_value(), 4)

    def test_05_SeverityNotice(self):
        """
        Test SeverityUnit with SeverityNotice
        """
        value = pykerio.enums.SeverityUnit(name='SeverityNotice')
        self.assertEqual(value.dump(), 'SeverityNotice')
        self.assertEqual(value.get_name(), 'SeverityNotice')
        self.assertEqual(value.get_value(), 5)

    def test_06_SeverityInformational(self):
        """
        Test SeverityUnit with SeverityInformational
        """
        value = pykerio.enums.SeverityUnit(name='SeverityInformational')
        self.assertEqual(value.dump(), 'SeverityInformational')
        self.assertEqual(value.get_name(), 'SeverityInformational')
        self.assertEqual(value.get_value(), 6)

    def test_07_SeverityDebug(self):
        """
        Test SeverityUnit with SeverityDebug
        """
        value = pykerio.enums.SeverityUnit(name='SeverityDebug')
        self.assertEqual(value.dump(), 'SeverityDebug')
        self.assertEqual(value.get_name(), 'SeverityDebug')
        self.assertEqual(value.get_value(), 7)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test SeverityUnit with FAIL
        """
        value = pykerio.enums.SeverityUnit(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
