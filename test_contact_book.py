"""Initial tests created by Developer A."""

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


def run_tests() -> int:
    """Run all test groups and return the failure count."""
    tests = [test_add_and_list_contacts, test_duplicate_email, test_invalid_contact]
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
