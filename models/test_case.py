from dataclasses import dataclass

@dataclass
class TestCase:
    test_case_title: str
    purpose: str
    expected_result: str