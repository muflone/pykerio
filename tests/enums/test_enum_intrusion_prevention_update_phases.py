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

from pykerio.enums import IntrusionPreventionUpdatePhases as IntrusionPrevUP


class TestCase_IntrusionPreventionUpdatePhases(unittest.TestCase):
    def test_00_IntrusionPreventionUpdateOk(self):
        """
        Test IntrusionPreventionUpdatePhases with IntrusionPreventionUpdateOk
        """
        value = IntrusionPrevUP.IntrusionPreventionUpdateOk
        self.assertEqual(value.dump(), 'IntrusionPreventionUpdateOk')
        self.assertEqual(value.name, 'IntrusionPreventionUpdateOk')
        self.assertEqual(value.value, 0)

    def test_01_IntrusionPreventionUpdateError(self):
        """
        Test IntrusionPreventionUpdatePhases with
        IntrusionPreventionUpdateError
        """
        value = IntrusionPrevUP.IntrusionPreventionUpdateError
        self.assertEqual(value.dump(), 'IntrusionPreventionUpdateError')
        self.assertEqual(value.name, 'IntrusionPreventionUpdateError')
        self.assertEqual(value.value, 1)

    def test_02_IntrusionPreventionUpdateProgress(self):
        """
        Test IntrusionPreventionUpdatePhases with
        IntrusionPreventionUpdateProgress
        """
        value = IntrusionPrevUP.IntrusionPreventionUpdateProgress
        self.assertEqual(value.dump(), 'IntrusionPreventionUpdateProgress')
        self.assertEqual(value.name, 'IntrusionPreventionUpdateProgress')
        self.assertEqual(value.value, 2)
