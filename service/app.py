"""Import Modules"""
# pylint: disable=C0103
from datetime import datetime
import argparse
from .boot_time import Boot
from .cpu import Cpu
from .disk import Disk
from .memory import Memory
from .network import Network
from .slack import Slack
from .system import System


# Setup arguments
parser = argparse.ArgumentParser(
    description='Service serves savvy server stats.')
parser.add_argument('-b', '--boot', action='store_true',
                    help='Show boot time stats.')
parser.add_argument('-c', '--cpu', action='store_true',
                    help='Show CPU stats.')
parser.add_argument('-d', '--disk', action='store_true',
                    help='Show disk stats.')
parser.add_argument('-m', '--memory', action='store_true',
                    help='Show memory stats.')
parser.add_argument('-n', '--network', action='store_true',
                    help='Show network stats.')
parser.add_argument('-s', '--system', action='store_true',
                    help='Show system stats.')
parser.add_argument('-sl', '--slack', action='store_true',
                    help='Send Service report to Slack.')
args = parser.parse_args()


def main():
    """Run the Service app"""
    # Preamble
    service_message = '='*15 + ' SERVICE ' + '=' * \
        15 + '\n' + f'Service Report ({datetime.now()})\n{args}'
    print(service_message)

    # Serve boot time data
    if args.boot is True:
        boot = Boot.serve()
        print(boot)

    # Serve CPU data
    if args.cpu is True:
        cpu = Cpu.serve()
        print(cpu)

    # Serve disk data
    if args.disk is True:
        disk = Disk.serve()
        print(disk)

    # Serve memory data
    if args.memory is True:
        memory = Memory.serve()
        print(memory)

    # Serve network data
    if args.network is True:
        network = Network.serve()
        print(network)

    # Serve system data
    if args.system is True:
        system = System.serve()
        print(system)

    # Send Slack message
    if args.slack is True:
        final_message = '\n' + service_message + '\n' + boot + '\n' + \
            system + '\n' + cpu + '\n' + disk + '\n' + memory + '\n' + network
        slack = Slack.message(final_message)
        print(slack)


if __name__ == '__main__':
    main()
