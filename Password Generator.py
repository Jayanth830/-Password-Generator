import random
import string


def generate_password(length=12):
    """Generate a strong password of a given length."""
    if length < 4:  # Ensure minimum length to include all character types
        raise ValueError("Password length should be at least 4 characters.")

    # Characters to use in passwords
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure the password includes at least one character from each character type
    all_characters = lowercase + uppercase + digits + punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Generate and print a strong password of default length 12
print(generate_password())

# Generate and print a strong password of length 16
print(generate_password(16))
