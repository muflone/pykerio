##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import os
import ssl
import unittest

import pykerio


class TestCase_Session(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Prepares Session tests
        """
        cls.username = os.environ.get('KERIO_USERNAME', 'admin-en')
        # Ignore invalid certificates
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        # API object
        api = pykerio.PyKerioControl(
            server=os.environ.get('KERIO_SERVER', 'control-demo.kerio.com'),
            port=int(os.environ.get('KERIO_PORT', '4081')))
        # Session object
        cls.session = pykerio.interfaces.Session(api)

    def test_01_login(self):
        """
        Test Session login
        """
        password = os.environ.get('KERIO_PASSWORD', 'kerio')
        application = pykerio.structs.ApiApplication({
            'name': self.__class__.__name__,
            'vendor': pykerio.constants.APP_NAME,
            'version': pykerio.constants.APP_VERSION})
        self.__class__.session.login(userName=self.username,
                                     password=password,
                                     application=application)
        self.assertNotEquals(self.__class__.session.api.token, '')

    def test_02_getUserName(self):
        """
        Test Session username
        """
        self.assertNotEquals(self.__class__.session.api.token, '')
        self.assertEquals(self.__class__.session.getUserName(), self.username)

    def test_03_getCsrfToken(self):
        """
        Test Session Csrf token
        """
        self.assertNotEquals(self.__class__.session.getCsrfToken(), '')

    def test_04_getLoginType(self):
        """
        Test Session login type
        """
        self.assertEquals(self.__class__.session.getLoginType().dump(),
                          'LoginRegular')

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_05_apply(self):
        """
        Test Session apply
        """
        self.__class__.session.apply()

    def test_99_logout(self):
        """
        Test Session logout
        """
        self.__class__.session.logout()
