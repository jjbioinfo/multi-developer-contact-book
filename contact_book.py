"""Initial Contact Book implementation created by Developer A."""

import logging

from contact import Contact

logger = logging.getLogger(__name__)


class ContactBook:
    """Store contacts and provide basic contact operations."""

    def __init__(self) -> None:
        self._contacts: list[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """Add a contact when its email address is unique."""
        if not isinstance(contact, Contact):
            raise TypeError("contact must be a Contact object")
        if any(existing.email == contact.email for existing in self._contacts):
            raise ValueError(f"contact email {contact.email} already exists")
        self._contacts.append(contact)
        logger.info(f"Contact added: email={contact.email!r}")

    def list_contacts(self) -> tuple[Contact, ...]:
        """Return contacts without exposing the mutable internal list."""
        return tuple(self._contacts)
