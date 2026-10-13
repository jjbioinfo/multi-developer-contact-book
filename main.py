"""Demonstrate Developer B's contact-search feature."""

from contact import Contact
from contact_book import ContactBook


def main() -> int:
    """Create and display example contacts."""
    contact_book = ContactBook()
    contact_book.add_contact(Contact("Asha", "asha@example.com", "555-0101"))
    contact_book.add_contact(Contact("Rahul", "rahul@example.com", "555-0102"))

    print("ALL CONTACTS")
    for contact in contact_book.list_contacts():
        print(contact.display())
    print("\nSEARCH RESULTS FOR ASHA")
    for contact in contact_book.search_contacts("ASHA"):
        print(contact.display())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
