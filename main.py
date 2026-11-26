from repositories.test_case_repository import TestCaseRepository
from services.test_case_service import TestCaseService
from dialogs.test_case_dialog import TestCaseDialog

test_case_repository = TestCaseRepository()
test_case_service = TestCaseService(test_case_repository)
test_case_dialog = TestCaseDialog(test_case_service)

def main() -> None:
    test_case_dialog.main_menu()

if __name__ == "__main__":
    main()
