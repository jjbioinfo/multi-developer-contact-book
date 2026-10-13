"""Base behavior and Developer B contact-search tests."""

from contact import Contact
from contact_book import ContactBook


def test_add_and_list_contacts() -> None:
    contact_book = ContactBook()
    contact = Contact("Asha", "asha@example.com", "555-0101")
    contact_book.add_contact(contact)
    assert contact_book.list_contacts() == (contact,)


def test_duplicate_email() -> None:
    contact_book = ContactBook()
    contact_book.add_contact(Contact("Asha", "asha@example.com", "555-0101"))
    try:
        contact_book.add_contact(Contact("Other", "asha@example.com", "555-9999"))
        raise AssertionError("duplicate email should fail")
    except ValueError:
        pass


def test_invalid_contact() -> None:
    for arguments in (
        ("", "asha@example.com", "555-0101"),
        ("Asha", "invalid-email", "555-0101"),
        ("Asha", "asha@example.com", ""),
    ):
        try:
            Contact(*arguments)
            raise AssertionError(f"invalid contact should fail: {arguments!r}")
        except ValueError:
            pass



def test_search_contacts() -> None:
    book = ContactBook()
    assert book.search_contacts("asha") == ()
    asha = Contact("Asha Rao", "asha@example.com", "555-0101")
    rahul = Contact("Rahul", "rahul@example.com", "555-0102")
    unicode_contact = Contact("Straße", "street@example.org", "555-0103")
    for contact in (asha, rahul, unicode_contact):
        book.add_contact(contact)
    assert book.search_contacts("  ASHA  ") == (asha,)
    assert book.search_contacts("RAO") == (asha,)
    assert book.search_contacts("EXAMPLE.COM") == (asha, rahul)
    assert book.search_contacts("STRASSE") == (unicode_contact,)
    assert book.search_contacts("not-present") == ()
    assert book.list_contacts() == (asha, rahul, unicode_contact)
    for invalid, expected in (("", ValueError), ("   ", ValueError),
                              (None, TypeError), (25, TypeError)):
        try:
            book.search_contacts(invalid)
        except expected:
            pass
        else:
            raise AssertionError(f"invalid query accepted: {invalid!r}")

def run_tests() -> int:
    """Run all test groups and return the failure count."""
    tests = [test_add_and_list_contacts, test_duplicate_email, test_invalid_contact, test_search_contacts]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except Exception as error:
            failures += 1
            print(f"FAIL: {test.__name__}: {error}")
    print(f"Ran {len(tests)} test groups; failures={failures}")
    return failures


if __name__ == "__main__":
    raise SystemExit(run_tests())
