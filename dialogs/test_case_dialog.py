from dataclasses import dataclass

from utils.console_helper import pause, clear_screen, required_input
from services.test_case_service import TestCaseService
from models.test_case import TestCase

@dataclass
class TestCaseDialog:
    __service: TestCaseService

    def main_menu(self) -> None:

        while True:
            clear_screen()

            print("")
            print("### TEST CASE REGISTRATOR ###")
            print("1. Create a test case")
            print("2. Show a list of test cases")
            print("0. Exit")

            option = input("\nChoose an option: ").strip()

            match option:

                case "1":
                    self.show_create_test_case()

                case "2":
                    self.show_test_cases()

                case "0":
                    return

                case _:
                    print("\nINVALID OPTION. Please try again!")
                    pause()

    def show_create_test_case(self) -> None:

        clear_screen()

        test_case_title = required_input("\nEnter test case title: ").strip()
        purpose = required_input("Enter purpose: ").strip()
        expected_result = required_input("Enter expected result: ").strip()

        test_case = TestCase(test_case_title, purpose, expected_result)

        try:
            self.__service.create_test_case(test_case)
            print("\nTest case successfully created!")

        except ValueError as error:
            print(error)

        pause()

    def show_test_cases(self) -> None:

        clear_screen()

        test_cases = self.__service.get_test_cases()

        if not test_cases:
            print("\nNo test cases have been saved yet.")

        else:
           for test_case in test_cases:
            print("")
            print("### TEST CASE ###")
            print(f"Test case title: {test_case.test_case_title}")
            print(f"Purpose: {test_case.purpose}")
            print(f"Expected result: {test_case.expected_result}")

        pause()
