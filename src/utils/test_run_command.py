from subprocess import SubprocessError
from unittest import TestCase

from utils.run_command import run_command


class TestRunCommand(TestCase):

	def test_echo(self):
		output, error = run_command(['echo', 'abc'])
		self.assertEqual(output, "abc")
		self.assertEqual(error, "")

	def test_error(self):
		with self.assertRaises(SubprocessError):
			run_command(['ls', '-error'])

	def test_sleep(self):
		output, error = run_command(['bash', '-c', 'sleep 0.5; echo "abc"'])
		self.assertEqual(output, "abc")
		self.assertEqual(error, "")
