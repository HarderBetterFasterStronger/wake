import unittest

from wake import up

class HandlerTest(unittest.TestCase):

  def test_event_failsWithNumberAsEvent(self):
    response = up(1, 2)
    self.assertEqual(response.get('statusCode'), 200)
    self.assertTrue(isinstance(response.get('body'), str))
