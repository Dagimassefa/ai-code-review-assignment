# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):
    valid_count = 0
    for email in emails:
        if not isinstance(email, str):
            continue
        email = email.strip()
        if not email:
            continue
        # Basic structural validation of email
        if email.count("@") != 1:
            continue
        local, domain = email.split("@")
        if not local or not domain:
            continue
        # check if it is a valid domain address
        if "." not in domain or domain.startswith(".") or domain.endswith("."):
            continue
        valid_count += 1

    return valid_count
