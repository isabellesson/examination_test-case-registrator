from models.test_case import TestCase

class TestCaseRepository:
    def __init__(self):
        self.__test_cases: list[TestCase] = []
    
    def add_create_test_case(self, test_case: TestCase) -> None: 
        self.__test_cases.append(test_case) 

    def get_all_test_cases(self) -> list[TestCase]:
        return self.__test_cases.copy() 


# Self = varje objekt kan komma åt sina egna attribut och metoder
# -> None = metoden returnerar inte något värde.
# Append = lägger till ett nytt testfall sist i listan self.__test_cases.
# Copy = skapar en kopia av listan och returnerar kopian istället för den ursprungliga listan.