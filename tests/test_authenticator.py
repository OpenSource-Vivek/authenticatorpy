#!/usr/bin/env python

import unittest
from authenticatorpy.authenticator import Authenticator

class AuthenticatorTest(unittest.TestCase):

    def setUp(self):
        self._authenticator = Authenticator('abcd xyzw abcd xyzw abcd xyzw abcd xyzw')

    def test_initiation(self):
        self.assertIsInstance(self._authenticator, Authenticator)
    
    def test_remove_spaces(self):
        string_without_spaces = self._authenticator.remove_spaces('abcd xyzw abcd xyzw abcd xyzw abcd xyzw')
        self.assertEqual(string_without_spaces, 'abcdxyzwabcdxyzwabcdxyzwabcdxyzw')
        string_without_spaces = self._authenticator.remove_spaces('abcd \tyzw \nbcd \tyzw')
        self.assertEqual(string_without_spaces, 'abcdyzwbcdyzw')
    
    def test_to_upper_case(self):
        upper_case_str = self._authenticator.to_upper_case('abcd')
        self.assertEqual(upper_case_str, 'ABCD')
        upper_case_str = self._authenticator.to_upper_case('aBcD')
        self.assertEqual(upper_case_str, 'ABCD')

    def test_decode_with_base32(self):
        decoded_str = self._authenticator.decode_with_base32('ABCDXYZWABCDXYZWABCDXYZWABCDXYZW')
        self.assertEqual(decoded_str, b'\x00D;\xe36\x00D;\xe36\x00D;\xe36\x00D;\xe36')

    def test_current_timestamp(self):
        self.assertIsNotNone(self._authenticator.current_timestamp())

    def test_create_hmac(self):
        decoded_str = self._authenticator.decode_with_base32('ABCDXYZWABCDXYZWABCDXYZWABCDXYZW')
        input = self._authenticator.current_timestamp() / 30
        hmac = self._authenticator.create_hmac(decoded_str, input)
        self.assertIsNotNone(hmac)

    def test_one_time_password(self):
        password = self._authenticator.one_time_password()
        self.assertIsNotNone(password)
