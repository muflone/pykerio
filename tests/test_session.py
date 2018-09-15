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
import pykerio.kerio


class TestCase_Session(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Prepares Session tests
        """
        cls.username = os.environ.get('KERIO_USERNAME', '')
        # Ignore invalid certificates
        ssl._create_default_https_context = ssl._create_unverified_context
        # API object
        api = pykerio.PyKerioControl(server='firewall.cc32.local',
                                     port=4081)
        # Session object
        cls.session = pykerio.kerio.Session(api)

    def test_01_login(self):
        """
        Test Session login
        """
        password = os.environ.get('KERIO_PASSWORD', '')
        application = pykerio.kerio.ApiApplication(name=pykerio.APP_NAME,
                                                   vendor=pykerio.APP_AUTHOR,
                                                   version=pykerio.APP_VERSION)
        self.__class__.session.login(userName=self.username,
                                     password=password,
                                     application=application)
        self.assertNotEquals(self.__class__.session.api.token, '')

    def test_99_logout(self):
        """
        Test Session logout
        """
        self.__class__.session.logout()

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
        self.assertNotEquals(self.session.getCsrfToken(), '')

    def test_04_getLoginType(self):
        """
        Test Session login type
        """
        self.assertEquals(self.session.getLoginType().name, 'LoginRegular')
