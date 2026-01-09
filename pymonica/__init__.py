"""
PyMonica - Python client for Monica CRM API
"""

from .client import MonicaClient
from .contact_manager import ContactManager
from .quick_fact_manager import QuickFactManager
from .contact_information_manager import ContactInformationManager
from .address_manager import AddressManager
from .calls_manager import CallsManager
from .notes_manager import NotesManager
from .reminders_manager import RemindersManager
from .contact_information_extractor import ContactInformationExtractor

__version__ = "0.1.0"
__all__ = ["MonicaClient", "ContactManager", "QuickFactManager", "ContactInformationManager", "AddressManager", "CallsManager", "NotesManager", "RemindersManager", "ContactInformationExtractor"]

