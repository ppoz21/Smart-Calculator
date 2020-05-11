from string import ascii_letters


class SmartCalculator:

    def __init__(self):
        self.usr_input = None
        self.variables = {}
        self.operators = ['+', '-', '*', '/', '^']

    def check_command(self, command):
        if command == "/help":
            self.print_help()
        elif command == "/exit":
            return True
        else:
            print("Unknown command")
        return False

    def check_expression(self, expression):
        try:
            print(eval(expression))
        except SyntaxError:
            print("Invalid expression")
        except NameError:
            lista = expression.split(' ')
            i = 0
            error = False
            for char in lista:
                if char in self.variables:
                    lista[i] = str(self.variables[char])
                else:
                    if char not in self.operators:
                        try:
                            int(char)
                        except (NameError, ValueError):
                            print("Unknown variable")
                            error = True
                            break
                i += 1
            if not error:
                expression = ''.join(lista)
                self.check_expression(expression)
            else:
                pass

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
            elif self.usr_input.strip() in self.variables and '=' not in self.usr_input:
                print(self.variables[self.usr_input])
            elif '=' in self.usr_input:
                if self.usr_input.count('=') > 1:
                    print("Invalid assignment")
                else:
                    lista = self.usr_input.split('=')
                    for char in lista[0].strip():
                        if char not in ascii_letters:
                            print("Invalid identifier")
                        else:
                            if lista[1].strip() in self.variables:
                                self.variables[lista[0].strip()] = self.variables[lista[1].strip()]
                            else:
                                try:
                                    value = int(lista[1])
                                except ValueError:
                                    for char2 in lista[1]:
                                        if char2 not in ascii_letters:
                                            print("Invalid assignment")
                                            break
                                        else:
                                            print("Unknown variable")
                                else:
                                    self.variables[lista[0].strip()] = value
            else:
                self.check_expression(self.usr_input)
            self.usr_input = input()
        print("Bye!")


if __name__ == "__main__":
    calc = SmartCalculator()
    calc.main()
