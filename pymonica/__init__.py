"""
PyMonica - Python client for Monica CRM API
"""

from .client import MonicaClient
from .contact_manager import ContactManager
from .quick_fact_manager import QuickFactManager

__version__ = "0.1.0"
__all__ = ["MonicaClient", "ContactManager", "QuickFactManager"]

