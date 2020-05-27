import service

# Serve boot time data
service.Boot.serve()

# Serve CPU data
service.Cpu.serve()

# Serve disk data
service.Disk.serve()

# Serve memory data
service.Memory.serve()

# Serve network data
service.Network.serve()

# Serve system data
service.System.serve()
