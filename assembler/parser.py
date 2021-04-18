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
