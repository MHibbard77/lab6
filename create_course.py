import unittest


class CreateCourseTests(unittest.TestCase):
    def setup(self):
        self.ui.command("create_user Administrator")
        self.ui.command("create_user Supervisor")

    """
    When the create course cmd is entered, it takes < 3 > arguments:
    - Title
    - Instructor
    - Open TA slots
    If Title and Instructor fields are filled in, create course is a success:
    - "Create course successful."
    If Title field is omitted, failure:
    - "Error creating course."
    If Instructor field is omitted, failure:
    - "Error creating course."
    If Title already exists, failure:
    - "Error creating  course."
    """
