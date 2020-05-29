"""Import modules"""
# pylint: disable=R0903,R0914
import psutil
from .globals import Global


class Network():
    """Network information"""
    @classmethod
    def serve(cls):
        """Serve network info"""
        # Title
        network_title = '='*15 + ' Network Information ' + '='*15

        # Network information (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        all_pieces = ''
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                interface_title = f'=== Interface: {interface_name} ==='
                if str(address.family) == 'AddressFamily.AF_INET':
                    ip_address = f'  IP Address: {address.address}'
                    netmask = f'  Netmask: {address.netmask}'
                    broadcast_ip = f'  Broadcast IP: {address.broadcast}'
                    # Combine each piece into a variable
                    piece = ip_address + '\n' + netmask + '\n' + broadcast_ip
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    mac = f'  MAC Address: {address.address}'
                    netmask = f'  Netmask: {address.netmask}'
                    broadcast_mac = f'  Broadcast MAC: {address.broadcast}'
                    # Combine each piece into a variable
                    piece = mac + '\n' + netmask + '\n' + broadcast_mac
                # Combine each piece into a variable
                all_pieces += interface_title + '\n' + piece + '\n'

        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        sent = f'Total Bytes Sent: {Global.get_size(net_io.bytes_sent)}'
        received = f'Total Bytes Received: {Global.get_size(net_io.bytes_recv)}'

        final_message = '\n' + network_title + '\n' + \
            all_pieces + sent + '\n' + received
        return final_message
