#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, arg):
        return True
    def do_EOF(self, arg):
        return True
    def do_help(self, arg):
        super().do_help(arg)
    def do_emptyline(self):
        None
if __name__ == '__main__':
    HBNBCommand().cmdloop()