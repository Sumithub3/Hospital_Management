from django.test import TestCase

# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.Patient_Details.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 202)