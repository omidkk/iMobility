"""Flask configuration variables."""
import logging
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
