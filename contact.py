"""Contact model for the shared Contact Book project."""


def require_text(value: object, field_name: str) -> str:
    """Return non-empty text after removing surrounding spaces."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} cannot be empty")
    return cleaned_value


class Contact:
    """Represent one contact with a name, email, and phone number."""

    def __init__(self, name: str, email: str, phone: str) -> None:
        cleaned_email = require_text(email, "email")
        if cleaned_email.count("@") != 1:
            raise ValueError("email must contain one @ symbol")
        self.name = require_text(name, "name")
        self.email = cleaned_email
        self.phone = require_text(phone, "phone")

    def display(self) -> str:
        """Return the contact as readable text."""
        return f"{self.name} | {self.email} | {self.phone}"
