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

        assert parser.dest("D;JGT") == None
        assert parser.dest("M=1") == assembler_constants.M_DEST
        assert parser.dest("A=1") == assembler_constants.A_DEST
        assert parser.dest("D=1") == assembler_constants.D_DEST


        assert parser.comp("M=1") == "1"
        assert parser.comp("D=0") == "0"
        assert parser.comp("A=-1") == "-1"
        assert parser.comp("M=D") == "D"
        assert parser.comp("M=A") == "A"
        assert parser.comp("M=!D") == "!D"
        assert parser.comp("M=!A") == "!A"
        assert parser.comp("M=-D") == "-D"
        assert parser.comp("M=-A") == "-A"
        assert parser.comp("M=D+1") == "D+1"
        assert parser.comp("M=A+1") == "A+1"
        assert parser.comp("M=D-1") == "D-1"
        assert parser.comp("M=A-1") == "A-1"
        assert parser.comp("M=D+A") == "D+A"
        assert parser.comp("M=D-A") == "D-A"
        assert parser.comp("M=A-D") == "A-D"
        assert parser.comp("M=D&A") == "D&A"
        assert parser.comp("M=D|A") == "D|A"

        assert parser.comp("A=M") == "M"
        assert parser.comp("A=!M") == "!M"
        assert parser.comp("A=M+1") == "M+1"
        assert parser.comp("A=M-1") == "M-1"
        assert parser.comp("A=D+M") == "D+M"
        assert parser.comp("A=D-M") == "D-M"
        assert parser.comp("A=M-D") == "M-D"
        assert parser.comp("A=D&M") == "D&M"
        assert parser.comp("A=D|M") == "D|M"
