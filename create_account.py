import unittest


class CreateAccountTests(unittest.TestCase):
    def setup(self):
        self.ui.command("create_user Supervisor SupervisorPassword")
        self.ui.command("create_user Administrator AdministratorPassword")
        self.ui.command("create_user Instructor InstructorPassword")
        self.ui.command("create_user TA TAPassword")

    """
        Account creation requires user logged in as Supervisor or Administrator.
        When the create account command is entered, it takes three arguments:
            - Username
            - Password
            - email address
        If the username and password do not already exist in the database, account creation
        is successful:
        - "Account created successfully."
        If the username is already taken, failure:
        - "Username already taken."
        If the username or password is omitted, failure:
        - "Invalid arguments in command."
        If the user is not logged in as a Supervisor or Administrator, failure:
        - "You are not authorized to create accounts."
    """
