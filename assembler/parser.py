import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/assembler')
import assembler_constants

class Parser:

    def command_type(self, command):
        command = list(command)
        first_char = command[0]
        if first_char == "@":
            return assembler_constants.A_COMMAND
        elif first_char == '(':
            return assembler_constants.L_COMMAND
        else:
            return assembler_constants.C_COMMAND

    def symbol(self, command):
        command = list(command)
        first_char = command[0]

        if first_char == '@':
            return ''.join(command[1:])
        else:
            return ''.join(command[1:len(command)-1])

    def dest(self, command):
        command = list(command)

        try:
            has_dest = command.index('=')
            if has_dest is False:
                return None
        except ValueError:
            return None

        first_char = command[0]
        return first_char
