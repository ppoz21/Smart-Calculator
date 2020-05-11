from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class CalcTest(StageTest):
    def generate(self) -> List[TestCase]:
        cases = {"100 + 200 - 300\n/exit": "0\nBye!",
                 "4 + 6 - 8\n2 - 3 - 4\n/exit": "2\n-5\nBye!",
                 "8\n\n-2 + 4 - 5 + 6\n9 +++ 10 -- 8\n3 --- 5\n14     -  12\n/exit": "8\n3\n27\n-2\n2\nBye!"}
        return [TestCase(stdin=case,
                         attach=cases[case])
                for case in cases]

    def check(self, reply: str, attach) -> CheckResult:
        return CheckResult(reply.strip() == attach.strip(), "")


if __name__ == '__main__':
    CalcTest("calculator.calculator").run_tests()