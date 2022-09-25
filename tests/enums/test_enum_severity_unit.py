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

from pykerio.enums import SeverityUnit


class TestCase_SeverityUnit(unittest.TestCase):
    def test_00_SeverityEmergency(self):
        """
        Test SeverityUnit with SeverityEmergency
        """
        value = SeverityUnit.SeverityEmergency
        self.assertEqual(value.dump(), 'SeverityEmergency')
        self.assertEqual(value.name, 'SeverityEmergency')
        self.assertEqual(value.value, 0)

    def test_01_SeverityAlert(self):
        """
        Test SeverityUnit with SeverityAlert
        """
        value = SeverityUnit.SeverityAlert
        self.assertEqual(value.dump(), 'SeverityAlert')
        self.assertEqual(value.name, 'SeverityAlert')
        self.assertEqual(value.value, 1)

    def test_02_SeverityCritical(self):
        """
        Test SeverityUnit with SeverityCritical
        """
        value = SeverityUnit.SeverityCritical
        self.assertEqual(value.dump(), 'SeverityCritical')
        self.assertEqual(value.name, 'SeverityCritical')
        self.assertEqual(value.value, 2)

    def test_03_SeverityError(self):
        """
        Test SeverityUnit with SeverityError
        """
        value = SeverityUnit.SeverityError
        self.assertEqual(value.dump(), 'SeverityError')
        self.assertEqual(value.name, 'SeverityError')
        self.assertEqual(value.value, 3)

    def test_04_SeverityWarning(self):
        """
        Test SeverityUnit with SeverityWarning
        """
        value = SeverityUnit.SeverityWarning
        self.assertEqual(value.dump(), 'SeverityWarning')
        self.assertEqual(value.name, 'SeverityWarning')
        self.assertEqual(value.value, 4)

    def test_05_SeverityNotice(self):
        """
        Test SeverityUnit with SeverityNotice
        """
        value = SeverityUnit.SeverityNotice
        self.assertEqual(value.dump(), 'SeverityNotice')
        self.assertEqual(value.name, 'SeverityNotice')
        self.assertEqual(value.value, 5)

    def test_06_SeverityInformational(self):
        """
        Test SeverityUnit with SeverityInformational
        """
        value = SeverityUnit.SeverityInformational
        self.assertEqual(value.dump(), 'SeverityInformational')
        self.assertEqual(value.name, 'SeverityInformational')
        self.assertEqual(value.value, 6)

    def test_07_SeverityDebug(self):
        """
        Test SeverityUnit with SeverityDebug
        """
        value = SeverityUnit.SeverityDebug
        self.assertEqual(value.dump(), 'SeverityDebug')
        self.assertEqual(value.name, 'SeverityDebug')
        self.assertEqual(value.value, 7)
