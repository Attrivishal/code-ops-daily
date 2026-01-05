"""
Real-time system resource monitor
"""
import psutil
import time
import os
from colorama import init, Fore

class SystemMonitor:
    def __init__(self):
        init()  # Colorama init
    
    def display_dashboard(self):
        """Display real-time system dashboard"""
        os.system('clear')
        
        while True:
            print(Fore.CYAN + "=" * 60)
            print(Fore.YELLOW + "🖥️  REAL-TIME SYSTEM MONITOR")
            print(Fore.CYAN + "=" * 60)
            
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_cores = psutil.cpu_count()
            print(Fore.GREEN + f"CPU: {cpu_percent}% | Cores: {cpu_cores}")
            print(self._progress_bar(cpu_percent))
            
            # Memory
            memory = psutil.virtual_memory()
            print(Fore.GREEN + f"RAM: {memory.percent}% | {memory.used//(1024**3)}/{memory.total//(1024**3)} GB")
            print(self._progress_bar(memory.percent))
            
            # Disk
            disk = psutil.disk_usage('/')
            print(Fore.GREEN + f"Disk: {disk.percent}% | {disk.used//(1024**3)}/{disk.total//(1024**3)} GB")
            print(self._progress_bar(disk.percent))
            
            # Network
            net = psutil.net_io_counters()
            print(Fore.GREEN + f"Net: ↑ {net.bytes_sent//1024}KB | ↓ {net.bytes_recv//1024}KB")
            
            # Processes
            processes = len(psutil.pids())
            print(Fore.GREEN + f"Processes: {processes}")
            
            print(Fore.CYAN + "=" * 60)
            print(Fore.WHITE + "Press Ctrl+C to exit")
            
            time.sleep(2)
            os.system('clear')
    
    def _progress_bar(self, percent, length=30):
        """Create ASCII progress bar"""
        filled = int(length * percent / 100)
        bar = '█' * filled + '░' * (length - filled)
        return f"[{bar}] {percent:.1f}%"