from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.proceedings.api.proceedings import Proceedings


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
                proceedings check [HIDS]
                proceedings create
                proceedings delete
                proceedings clean
                proceedings list owners
                proceedings list paper1
                proceedings list paper2
                proceedings list project
                proceedings list hids

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print ("GGGG")
        p = Proceedings()
        c  = p.read_git_list(filename='list.txt')
        print (c)
        print ("GGGG")        
        print(arguments)
        if arguments.clone:
            print ("clone")
            hids = p.clone(filename='list.txt')


        elif arguments.list and arguments.hids:
            print(p.read_hid_list(filename='list.txt'))

        elif arguments.clean:
            hids = p.read_hid_list(filename='list.txt')
            for hid in hids:
                os.system ("rm -rf ../{hid}".format(hid=hid))


