from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class ProceedingsCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_proceedings(self, args, arguments):
        """
        ::

          Usage:
                proceedings -f FILE
                proceedings FILE
                proceedings list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



