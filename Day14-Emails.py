def read_emails():
    """
    Ask the user for names and emails to store in a database for emails. Note: this program is case-sensitive
    """
    emails = {}                   # Create empty email list

    while True:
        name = input("Name: ")
        if name == "":
            break
        email = input("Email: ")
        emails[name] = email

    return emails


def print_emails(emails):
    """
    Prints out all the names/numbers in the database.
    """
    for name in emails:
        print(name, "->", emails[name])


def lookup_emails(emails):
    """
    Allow the user to lookup emails in the database
    by looking up the email associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in emails:
            print(name + " is not included")
        else:
            print(name + "'s email is " + emails[name])


def main():
    email = read_emails()
    print_emails(email)
    lookup_emails(email)


if __name__ == '__main__':
    main()
