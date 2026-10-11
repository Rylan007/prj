import os
import sys

# Ensure project root is in sys.path so `backend` package resolves on Vercel
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.app import app

# Vercel looks for the WSGI `app` object
__all__ = ["app"]
