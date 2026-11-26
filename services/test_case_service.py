from models.test_case import TestCase
from repositories.test_case_repository import TestCaseRepository

class TestCaseService:
    def __init__(self, test_case_repository: TestCaseRepository):
        self.__repository: TestCaseRepository = test_case_repository

    def create_test_case(self, test_case: TestCase) -> None:

        # normalize
        test_case_title = test_case.test_case_title.strip()
        purpose = test_case.purpose.strip()
        expected_result = test_case.expected_result.strip()

        # validate
        if not test_case_title or not purpose or not expected_result:
            raise ValueError("\nAll fields are required.")

        # create
        new_test_case = TestCase(test_case_title, purpose, expected_result)

        # delegate
        self.__repository.add_create_test_case(new_test_case)

    def get_test_cases(self) -> list[TestCase]:

        # delegate
        test_cases = self.__repository.get_all_test_cases()

        # return
        return test_cases


# Self = varje objekt kan komma åt sina egna attribut och metoder
# -> None = metoden returnerar inte något värde.