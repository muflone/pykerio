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

from pykerio.enums import ApiEntity


class TestCase_ApiEntity(unittest.TestCase):
    def test_00_PolicyWizard(self):
        """
        Test ApiEntity with PolicyWizard
        """
        value = ApiEntity.PolicyWizard
        self.assertEqual(value.dump(), 'PolicyWizard')
        self.assertEqual(value.name, 'PolicyWizard')
        self.assertEqual(value.value, 0)

    def test_01_AlertList(self):
        """
        Test ApiEntity with AlertList
        """
        value = ApiEntity.AlertList
        self.assertEqual(value.dump(), 'AlertList')
        self.assertEqual(value.name, 'AlertList')
        self.assertEqual(value.value, 1)
