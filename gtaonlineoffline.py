import psutil
from time import sleep

for proc in psutil.process_iter():
    if "GTA5.exe" in proc.name():
       pid = proc.pid

p = psutil.Process(pid)
print('suspending..')
p.suspend()
sleep(10)
print('resuming')
p.resume()