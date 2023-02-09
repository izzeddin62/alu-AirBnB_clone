#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, arg):
        return True
    def help_quit(self):
        print("Quit command to exit the program")
    def do_EOF(self, arg):
        return True
    def help_EOF(self):
        print("EOF command to exit the program")
    def do_help(self, arg):
        super().do_help(arg)
    def help_help(self):
        print("help command to provide more information")
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
