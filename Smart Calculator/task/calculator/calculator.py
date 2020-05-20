import re


class Calculator:
    h = '''Smart Calculator
    The program calculate expressions like these: 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1), and so on.
    Calculator support variables, suppose that the name of a variable (identifier) can contain only Latin letters. 
    Supports user commands such as /exit and /help'''

    def __init__(self):
        self.data = ''
        self.vars = {}
        self.calc()

    def is_empty_line(self):
        """Check if a user enters an empty line, returns True or False"""
        return True if re.match(r'^\s*$', self.data) else False

    def is_single_number_or_variable(self):
        """Check if a user enters a single_number or variable, returns True or False"""
        dt = re.match(r'^\s*([a-zA-Z]+|-*\d+)\s*$', self.data)
        if dt:
            if dt.group(1).isalpha():  # if isn't digit print it
                print(self.vars.get(self.data.strip(), 'Unknown variable'))
            else:
                print(self.data)
            return True
        else:
            return False

    def is_command(self):
        """Check if a user enters a command, returns 0 - no action, 1 - break, 2 - continue"""
        dt = re.match(r'^\s*(/\w+)\s*$', self.data.lower())
        if dt:
            if dt.group(1) == '/exit':  # if "/exit" is entered, the program print "Bye!" and then stop
                print('Bye!')
                return 1  # break
            elif dt.group(1) == '/help':  # if "/help" is entered, than print some information about the program
                print(self.h)
            else:
                print('Unknown command')
            return 2  # continue
        return 0  # no actions

    def is_variable_assignment(self):
        """If the user wants to assign a value to a variable make it, returns True or False"""
        var_assign = re.match(r'^\s*(\d+|\w+)\s*=\s*(-*\d+|\w+)\s*(.*)', self.data)
        if var_assign:
            # if the first variable's name has a digit, then this is an invalid identifier
            if not var_assign.group(1).isalpha():
                print('Invalid identifier')
                return True

            # if the second variable's name has digits and chars together, then this is an invalid assignment
            if not var_assign.group(2).lstrip('-').isdigit() and not var_assign.group(2).lstrip('-').isalpha():
                print('Invalid assignment')
                return True

            # if there are something else after the second operand, then this is an invalid assignment too
            if var_assign.group(3):
                print('Invalid assignment')
                return True

            # if the second operand is the name of a variable, replace it with a value
            # otherwise the first operand will be assigned the second option (digital value)
            if var_assign.group(2).isalpha():
                var = self.vars.get(var_assign.group(2))
                if var is None:  # if the variable does not exist
                    print('Unknown variable')
                else:
                    self.vars[var_assign.group(1)] = var
            else:
                self.vars[var_assign.group(1)] = var_assign.group(2)
            return True  # continue
        else:
            return False  # it's not assignment

    def input_corrector(self):
        """Correcting and cleaning of user input.
           Returns list of correct digits and operators or None if something wrong"""
        if re.search(r'\s*[\d\w]+\s+[\d\w]+\s*', self.data):  # if input contained two or more digits without operators
            print('Invalid expression')
            return None

        # split the user input to the list
        list_of_data = re.findall(r'\d+|[a-zA-Z]+|[-+*/]+|[)(]+|\^', self.data)
        for i in range(len(list_of_data)):
            # the name can't contains chars and digits in conjunction, this is invalid expression
            if re.search(r'[a-zA-Z]+', list_of_data[i]) and re.search(r'[0-9]+', list_of_data[i]):
                print('Invalid expression2', list_of_data[i])
                return None

            # replace the variable name with its value
            if re.match(r'^[a-zA-Z]+$', list_of_data[i]):
                list_of_data[i] = self.vars.get(list_of_data[i])
                if list_of_data[i] is None:  # if the variable does not exist return None
                    print('Unknown variable')
                    return None

            # now here we have only digital values and operators
            # dirty work =)

            # the operator from two minuses is converted to plus
            if re.match(r'^\s*-{2}\s*$', list_of_data[i]):  # "--" => "+"
                list_of_data[i] = '+'

            # the operator from two minuses is converted to plus with minus
            if re.match(r'^\s*-{2}\s+-\s*$', list_of_data[i]):  # "-- -" => "+-"
                list_of_data[i] = '+-'

            # many operators to one with minus
            lod = re.match(r'^\s*([-+/*])+\s+-\s*$', list_of_data[i])  # "(-|+|/|*) -" => "one_operator-"
            if lod:
                list_of_data[i] = lod.group(1) + '-'

            # many operators to one
            list_of_data[i] = re.sub(r'[\s]+', '', list_of_data[i])  # kill all whitespace
            lod = re.match(r'^\s*([-+])+\s*$', list_of_data[i])
            if lod:
                list_of_data[i] = lod.group(1)

            # the power operator
            if list_of_data[i] == '^':
                list_of_data[i] = '**'

        return list_of_data

    def calc(self):
        while True:
            self.data = input()

            # if a user enters an empty line, the program should ignore it
            if self.is_empty_line():
                continue

            # if a user enters only a single number, the program should print the same number
            if self.is_single_number_or_variable():
                continue

            # if the user wants to assign a value to the variable, make it
            if self.is_variable_assignment():
                continue

            # check if a user enters a command and execute it
            ret = self.is_command()
            if ret == 1:  # if is_command returns 1, it means that we have /exit command
                break
            if ret == 2:
                continue

            # calculation
            correct_input = self.input_corrector()  # get a list of correct digits and operators
            # print(correct_input)  # debug output
            if correct_input is None:  # if something is wrong with user input try again
                continue
            # noinspection PyBroadException
            try:
                print(int(eval(''.join(correct_input))))  # not the best solution, but with input_corrector() works well
            except Exception:
                print('Invalid expression')


calc = Calculator()