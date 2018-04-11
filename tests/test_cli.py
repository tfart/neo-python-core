from unittest import TestCase

from neocore.bin import cli


class CliTestCase(TestCase):
    def test_address_to_scripthash(self):
        address = "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"
        scripthash = cli.address_to_scripthash(address)
        self.assertEqual(scripthash, b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9')

        address = "AK2nJJpJr6o664CWJKi1QRXjqeic2zRpxx"
        with self.assertRaises(cli.ConversionError):
            scripthash = cli.address_to_scripthash(address)

    def test_scripthash_to_address(self):
        scripthash = "0xe9eed8dc39332032dc22e5d6e86332c50327ba23"
        address = cli.scripthash_to_address(scripthash)
        self.assertEqual(address, "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y")

        scripthash = "e9eed8dc39332032dc22e5d6e86332c50327ba23"
        address = cli.scripthash_to_address(scripthash)
        self.assertEqual(address, "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y")

        scripthash = "0xe9eed8dc39332032dc22e5d6e86332c50327baxx"
        with self.assertRaises(cli.ConversionError):
            address = cli.scripthash_to_address(scripthash)
