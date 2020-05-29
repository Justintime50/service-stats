"""Import Modules"""
# pylint: disable=C0103
from datetime import datetime
import service

# Preamble
service_message = '='*15 + ' SERVICE ' + '=' * \
    15 + '\n' + f'Service Report ({datetime.now()})'
print(service_message)

# Serve boot time data
boot = service.Boot.serve()
print(boot)

# Serve CPU data
cpu = service.Cpu.serve()
print(cpu)

# Serve disk data
disk = service.Disk.serve()
print(disk)

# Serve memory data
memory = service.Memory.serve()
print(memory)

# Serve network data
network = service.Network.serve()
print(network)

# Serve system data
system = service.System.serve()
print(system)

# Send Slack message
final_message = '\n' + service_message + '\n' + boot + '\n' + system + '\n' + cpu + '\n' + disk + \
    '\n' + memory + '\n' + network
slack = service.Slack.message(final_message)
print(slack)
