# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Test cases for the key classes.
"""

from cinder.keymgr import key
from cinder import test


class KeyTestCase(test.TestCase):

    def _create_key(self):
        raise NotImplementedError()

    def setUp(self):
        super(KeyTestCase, self).setUp()

        self.key = self._create_key()


class SymmetricKeyTestCase(KeyTestCase):

    def _create_key(self):
        return key.SymmetricKey(self.algorithm, self.encoded)

    def setUp(self):
        self.algorithm = 'AES'
        self.encoded = [0] * 32

        super(SymmetricKeyTestCase, self).setUp()

    def test_get_algorithm(self):
        self.assertEqual(self.algorithm, self.key.get_algorithm())

    def test_get_format(self):
        self.assertEqual('RAW', self.key.get_format())

    def test_get_encoded(self):
        self.assertEqual(self.encoded, self.key.get_encoded())

    def test___eq__(self):
        self.assertTrue(self.key == self.key)

        self.assertFalse(self.key is None)
        self.assertFalse(None == self.key)

    def test___ne__(self):
        self.assertFalse(self.key != self.key)

        self.assertTrue(self.key is not None)
        self.assertTrue(None != self.key)
