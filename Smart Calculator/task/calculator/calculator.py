class SmartCalculator:

    def __init__(self):
        self.usr_input = None

    def check_command(self, command):
        if command == "/help":
            self.print_help()
        elif command == "/exit":
            return True
        else:
            print("Unknown command")
        return False

    @staticmethod
    def check_expression(expression):
        try:
            print(eval(expression))
        except (SyntaxError, NameError):
            print("Invalid expression")

    @staticmethod
    def print_help():
        print("The program calculates the sum and difference of numbers. Type '/exit' to exit")

    def main(self):
        self.usr_input = input()
        while True:
            if len(self.usr_input) == 0:
                pass
            elif self.usr_input.startswith("/"):
                to_break = self.check_command(self.usr_input)
                if to_break:
                    break
            else:
                self.check_expression(self.usr_input)
            self.usr_input = input()
        print("Bye!")


if __name__ == "__main__":
    calc = SmartCalculator()
    calc.main()
