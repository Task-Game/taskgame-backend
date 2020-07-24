from app.main.config import *
from manager import app

from flask_testing import TestCase
from flask import current_app
from os import getenv

import os
import unittest

from dotenv import load_dotenv
load_dotenv(dotenv_path="../../.env")


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.Development')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'eu_odeio_bts')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.Testing')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'eu_odeio_bts')
        self.assertTrue(app.config['DEBUG'] is True)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.Production')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == "__main__":
    unittest.main()
