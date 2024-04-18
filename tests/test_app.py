import pytest
from flask_testing import TestCase
from app import application

class TestBase(TestCase):
    """
    Base test case class for the application.
    """

    def create_app(self):
        """
        Create and return the Flask application.
        """
        return application

class TestRoutes(TestBase):
    """
    Test case class for testing the routes of the application.
    """

    def test_root_route(self):
        """
        Test the root route ("/") of the application.
        """
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"This is my Assignment Task!" in response.data # Updated assertion

    def test_help_route(self):
        """
        Test the help route ("/help") of the application.
        """
        response = self.client.get("/help")
        assert response.status_code == 200
        assert b"THIS IS HELP PAGE" in response.data # Updated assertion

    def test_hello(self):
        """
        Test the hello route ("/hello") of the application.
        """
        response = self.client.get("/hello")
        self.assert200(response)
        self.assertEqual(response.data.decode(), "Hello World from Flask Hello Page.<b> v1.0")
