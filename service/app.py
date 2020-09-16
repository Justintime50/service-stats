from datetime import datetime
import argparse
from service.stats.boot_time import Boot
from service.stats.cpu import Cpu
from service.stats.disk import Disk
from service.stats.memory import Memory
from service.stats.network import Network
from service.stats.system import System
from service.slack import Slack


class ServiceCLI():
    def __init__(self):
        """Setup CLI args
        """
        parser = argparse.ArgumentParser(
            description='Service serves savvy server stats.'
        )
        parser.add_argument(
            '-b',
            '--boot',
            action='store_true',
            required=False,
            default=False,
            help='Show boot time stats.'
        )
        parser.add_argument(
            '-c',
            '--cpu',
            action='store_true',
            required=False,
            default=False,
            help='Show CPU stats.'
        )
        parser.add_argument(
            '-d',
            '--disk',
            action='store_true',
            required=False,
            default=False,
            help='Show disk stats.'
        )
        parser.add_argument(
            '-m',
            '--memory',
            action='store_true',
            required=False,
            default=False,
            help='Show memory stats.'
        )
        parser.add_argument(
            '-n',
            '--network',
            action='store_true',
            required=False,
            default=False,
            help='Show network stats.'
        )
        parser.add_argument(
            '-s',
            '--system',
            action='store_true',
            required=False,
            default=False,
            help='Show system stats.'
        )
        parser.add_argument(
            '-sl',
            '--slack',
            action='store_true',
            required=False,
            default=False,
            help='Send Service report to Slack.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        Service.run(
            boot=self.boot,
            cpu=self.cpu,
            disk=self.disk,
            memory=self.memory,
            network=self.network,
            system=self.system,
            slack=self.slack,
        )


class Service():
    @classmethod
    def serve_data(cls, data_type):
        """Serve data from the specified category
        """
        data = data_type.serve()
        print(data)
        return data

    @classmethod
    def run(cls, boot=True, cpu=False, disk=False, memory=False,
            network=False, system=False, slack=False):
        """Run the Service app
        """
        # Preamble
        service_message = '='*15 + ' SERVICE ' + '=' * \
            15 + '\n' + f'Service Report ({datetime.now()})'
        print(service_message)

        if boot is True:
            boot_message = cls.serve_data(Boot)
        if cpu is True:
            cpu_message = cls.serve_data(Cpu)
        if disk is True:
            disk_message = cls.serve_data(Disk)
        if memory is True:
            memory_message = cls.serve_data(Memory)
        if network is True:
            network_message = cls.serve_data(Network)
        if system is True:
            system_message = cls.serve_data(System)

        final_message = (
            f'\n{service_message if service_message else ""}'
            f'\n{boot_message if boot_message else ""}'
            f'\n{system_message if system_message else ""}'
            f'\n{cpu_message if cpu_message else ""}'
            f'\n{disk_message if disk_message else ""}'
            f'\n{memory_message if memory_message else ""}'
            f'\n{network_message if network_message else ""}'
        )

        if slack is True:
            slack = Slack.message(final_message)
            print(slack)

        return final_message


def main():
    ServiceCLI().run()


if __name__ == '__main__':
    main()
