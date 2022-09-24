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


class TestCase_IntrusionPreventionAction(unittest.TestCase):
    def test_00_IntrusionPreventionAction_IntrusionPreventionActionDropAndLog(self):
        """
        Test IntrusionPreventionAction with IntrusionPreventionActionDropAndLog
        """
        value = pykerio.enums.IntrusionPreventionAction(name='IntrusionPreventionActionDropAndLog')
        self.assertEqual(value.dump(), 'IntrusionPreventionActionDropAndLog')
        self.assertEqual(value.get_name(), 'IntrusionPreventionActionDropAndLog')
        self.assertEqual(value.get_value(), 0)

    def test_01_IntrusionPreventionAction_IntrusionPreventionActionLog(self):
        """
        Test IntrusionPreventionAction with IntrusionPreventionActionLog
        """
        value = pykerio.enums.IntrusionPreventionAction(name='IntrusionPreventionActionLog')
        self.assertEqual(value.dump(), 'IntrusionPreventionActionLog')
        self.assertEqual(value.get_name(), 'IntrusionPreventionActionLog')
        self.assertEqual(value.get_value(), 1)

    def test_02_IntrusionPreventionAction_IntrusionPreventionActionNothing(self):
        """
        Test IntrusionPreventionAction with IntrusionPreventionActionNothing
        """
        value = pykerio.enums.IntrusionPreventionAction(name='IntrusionPreventionActionNothing')
        self.assertEqual(value.dump(), 'IntrusionPreventionActionNothing')
        self.assertEqual(value.get_name(), 'IntrusionPreventionActionNothing')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_IntrusionPreventionAction_FAIL(self):
        """
        Test IntrusionPreventionAction with FAIL
        """
        value = pykerio.enums.IntrusionPreventionAction(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
