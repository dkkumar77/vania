import datetime
import os
import platform
import psutil
import socket
import stat

# Logging Functions
def log_event(event):
    if not os.path.exists("../event_log.txt"):
        with open("../event_log.txt", "w") as log_file:
            log_file.write("Log File Created\n")
        os.chmod("event_log.txt", stat.S_IREAD)
    with open("../event_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {event}\n")




# System Information



def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
    return f"{bytes:.2f}Y{suffix}"



def system_info():
    log_event("Fetching system information")
    
    # Platform information
    print("\nPlatform Information:")
    print("-" * 40)
    print(f"Architecture:            {platform.architecture()}")
    print(f"Machine:                 {platform.machine()}")
    print(f"Node (Hostname):         {platform.node()}")
    print(f"Platform:                {platform.platform()}")
    print(f"Processor:               {platform.processor()}")
    print(f"Release:                 {platform.release()}")
    print(f"Version:                 {platform.version()}")
    print(f"Python Version:          {platform.python_version()}")
    print(f"Python Implementation:   {platform.python_implementation()}\n")
    
    # CPU information
    print("CPU Information:")
    print("-" * 40)
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores:    {psutil.cpu_count(logical=True)}")
    print("CPU usage per core:")
    # Note: The first call to psutil.cpu_percent() may be 0.0 if no interval is specified,
    # so an interval of 1 second is provided for per-core percentages.
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i}: {percentage}%")
    print(f"Total CPU usage: {psutil.cpu_percent()}%\n")
    
    # Disk information
    print("Disk Information:")
    print("-" * 40)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            print("  Permission Denied")
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used:       {get_size(partition_usage.used)}")
        print(f"  Free:       {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%\n")



system_info()



def check_cpu_usage():
    log_event("Checking CPU usage")
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}% / 100% ")


check_cpu_usage()

def check_memory_usage():
    log_event("Checking memory usage")
    memory = psutil.virtual_memory()
    print(f"Total memory: {memory.total / (1024 ** 3):.2f} GB, Available memory: {memory.available / (1024 ** 3):.2f} GB")

def check_disk_usage():
    log_event("Checking disk usage")
    disk = psutil.disk_usage('/')
    print(f"Total disk space: {disk.total / (1024 ** 3):.2f} GB, Free disk space: {disk.free / (1024 ** 3):.2f} GB")

# Network Functions
def check_network_usage():
    log_event("Checking network usage")
    net_io = psutil.net_io_counters()
    print(f"Bytes sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB, Bytes received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

def get_ip_address():
    log_event("Fetching IP address")
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"IP Address: {ip_address}")

def ip_flush():
    log_event("Flushing IP")
    if platform.system() == "Windows":
        os.system("ipconfig /release && ipconfig /renew")
    else:
        os.system("sudo ifconfig en0 down && sudo ifconfig en0 up")

def dns_lookup(domain):
    log_event(f"Performing DNS lookup for {domain}")
    if platform.system() == "Windows":
        os.system(f"nslookup {domain}")
    else:
        os.system(f"dig {domain}")

def ping_test(ip):
    log_event(f"Pinging {ip}")
    if platform.system() == "Windows":
        os.system(f"ping {ip} -n 4")
    else:
        os.system(f"ping {ip} -c 4")
