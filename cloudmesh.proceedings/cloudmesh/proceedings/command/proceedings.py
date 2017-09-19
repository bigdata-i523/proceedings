from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.proceedings.api.proceedings import Proceedings
from pprint import pprint
from cloudmesh.common.Printer import Printer

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
                proceedings list ATTRIBUTE [HID]

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        # print ("GGGG")
        p = Proceedings()
        c  = p.read_git_list(filename='list.txt')
        # print (c)
        # print ("GGGG")
        pprint(arguments)
        if arguments.clone:
            hids = p.clone(filename='list.txt')

        elif arguments.commit:
            msg = arguments.MESSAGE
            p.commit(filename='list.txt', msg=msg)
            p.push(filename='list.txt')

        elif arguments.pull:
            hids = p.pull(filename='list.txt')

        elif arguments.list and arguments.hids:
            print(p.read_hid_list(filename='list.txt'))

        elif arguments.clean:
            p.clean()

        elif arguments.list and arguments.ATTRIBUTE:
            hid = arguments.HID
            if hid is not None:
                # print(p.readme(hid))
                print("Owner Data Found")
                ok, missing = p.attribute(hid, arguments.ATTRIBUTE)
                print("\n".join(ok))
                print()
                # print ("Owner Data Missing")
                # print ("\n".join(missing))
            else:

                ok, missing = p.attribute(None, arguments.ATTRIBUTE)
                pprint (ok)
                pprint (missing)
                print(Printer.write(ok, order=['hid', 'name', 'url']))




