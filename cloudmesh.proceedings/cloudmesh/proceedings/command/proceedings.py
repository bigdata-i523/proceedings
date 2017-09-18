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
                proceedings clone [git=BASE] [HIDS]
                proceedings pull
                proceedings commit MESSAGE
                proceedings commit MESSAGE
                proccedings check [HIDS]
                proccedings create
                proccedings delete
                proccedings clean
                proccedings list owners
                proccedings list paper1
                proccedings list paper2
                proccedings list project
                proceedings list HIDS

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



