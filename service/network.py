"""Import modules"""
# pylint: disable=R0903
import psutil
from .globals import Global


class Network():
    """Network information"""
    @classmethod
    def serve(cls):
        """Serve network info"""
        # Network information
        print("="*40, "Network Information", "="*40)
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {Global.get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {Global.get_size(net_io.bytes_recv)}")
