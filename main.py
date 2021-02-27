import os
import psutil
import time
import socket
import shutil
import platform
import wmi
import math

# ------------------ İşletim sistemi bilgisi--------------#
if os.name == 'nt':
    print('İşletim Sistemi : Windows')
elif os.name == 'posix':
    print('İşletim Sistemi : Linux')

# ------------------ Bilgisayar adı alma------------------#
print("Bilgisayarın Adı : " + socket.gethostname())

# ------------------ Memory Güncel percent----------------#
a = psutil.virtual_memory()
print("Ram Güncel Kullanım : " + str(a[2]))

# ------------------ Hard Disk Kullanımı Percent----------#
a = psutil.disk_usage('/')
print("Harddisk Doluluk Oranı : " + str(a[3]))

# ------------------ cpu güncel kullanım-------------------#


a = psutil.cpu_percent(interval=None)
print("Cpu Güncel Kullanım : " + str(a))

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

print('İşlemci Adı  : {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(math.ceil(system_ram)))
print('Ekran Kartı : {0}'.format(gpu_info.Name))

# ------------------ Harddisk Boyutu-----------------------#

total, used, free = shutil.disk_usage("/")

print("Harddisk: {} GB".format((total // (2 ** 30))))
