"""Config for loading our environment upon server startup."""

import os


class Config:
    """Config class for accomplishing the environment loading."""

    ALLOWED_ORIGINS = os.environ["CORS_ORIGINS"]
