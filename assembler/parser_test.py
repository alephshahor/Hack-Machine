import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/assembler')
import assembler_constants
from parser import Parser

assembly_program = [
        ["@i"],
        ["M=1"],
        ["@sum"],
        ["M=0"],
        ["@i"],
        ["D=M"],
        ["@100"],
        ["D=D-A"],
        ["@END"],
        ["D;JGT"],
        ["@i"],
        ["D=M"],
        ["@sum"],
        ["M=D+M"],
        ["@i"],
        ["M=M+1"],
        ["@LOOP"],
        ["0;JMP"],
        ["@END"],
        ["0;JMP"]
    ]

parser = Parser()

def test_parser():

        in_ = ["@i", "(LOOP)", "M=1"]
        assert parser.command_type(in_[0]) == assembler_constants.A_COMMAND
        assert parser.command_type(in_[1]) == assembler_constants.L_COMMAND
        assert parser.command_type(in_[2]) == assembler_constants.C_COMMAND

        assert parser.symbol(in_[0]) == "i"
        assert parser.symbol(in_[1]) == "LOOP"
