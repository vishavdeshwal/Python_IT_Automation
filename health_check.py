

import shutil
import psutil

def check_disk_usage(disk): 
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(f"Free disk space: {free:.2f}%")
    # Python itself detects the moment we put comparision operator, it will eventually return boolean, unlike java where
       # we have to explicitly return boolean
    return free > 20
    

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print(f"CPU usage: {usage}%")
    # Python itself detects the moment we put comparision operator, it will eventually return boolean, unlike java where
       # we have to explicitly return boolean
    
    return usage < 75

print(check_cpu_usage())

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("Everything is ok")