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


class TestCase_ApiException(unittest.TestCase):
    def test_01_ApiException(self):
        """
        Test ApiException
        """
        positional_parameters = pykerio.lists.StringList()
        positional_parameters.append('User1')
        positional_parameters.append('Foo')

        message = 'Would you want to delete the user %1 (%2)?'
        messageparameters = pykerio.structs.LocalizableMessageParameters({
            'positionalParameters': positional_parameters,
            'plurality': 1})
        code = 32614
        teststruct = pykerio.structs.ApiException({
            'message': message,
            'code': code,
            'messageParameters': messageparameters})
        self.assertEqual(len(teststruct.keys()), 3)
        self.assertEqual(len(teststruct.values()), 3)

        self.assertEqual(teststruct['message'], message)
        self.assertEqual(teststruct['code'], code)
        self.assertEqual(teststruct['messageParameters'],
                         messageparameters)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
