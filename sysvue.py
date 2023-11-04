from cpuinfo import get_cpu_info
import platform
from psutil import virtual_memory, swap_memory
import click

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
@click.group()
def cli():
    pass

def display_info(dictionary):
    for key, val in dictionary.items():
        if key=="flags":
            continue
        else:
            print(f"{GREEN}{key}:-----{BLINK}>>  {END}{YELLOW}{val}{END}")



def get_cpu():
    info=get_cpu_info()
    return info


def get_mem():
    memory_info={
        "Total_Memory(RAM)":virtual_memory().total,
        "available":virtual_memory().available,
        "percent":virtual_memory().percent,
        "free":virtual_memory().free,
        "Total_Memory(SWAP)":swap_memory().total,
        "percent":swap_memory().percent,
        "free":swap_memory().free,
    }
    return memory_info

def get_sys():
    sys_info={
        "system":platform.system(),
        "machine":platform.machine(),
        "net_name":platform.node(),
        "processor":platform.processor(),
        "release":platform.release(),
        "version":platform.version()
    }
    return sys_info
@cli.command(help="view system info")
def sys():
    print(f"{RED}{BOLD}------------------------------*SYSTEM INFORMATION*----------------------------{END}")
    display_info(get_sys())

@cli.command(help="view CPU info")
def cpu():
    info=get_cpu()
    print(f"{RED}{BOLD}------------------------------*CPU INFORMATION*----------------------------{END}")  
    display_info(info)

@cli.command(help="view memory info")
def mem():
    memory=get_mem()
    print(f"{RED}{BOLD}------------------------------*MEMORY INFORMATION*----------------------------{END}")
    display_info(memory)



@cli.command(help="view all the information")
def all():
    cpu_info=get_cpu()
    print(f"{RED}{BOLD}------------------------------*CPU INFORMATION*----------------------------{END}")  
    display_info(cpu_info)

    print(f"{RED}{BOLD}------------------------------*SYSTEM INFORMATION*----------------------------{END}")
    display_info(get_sys())

    memory=get_mem()
    print(f"{RED}{BOLD}------------------------------*MEMORY INFORMATION*----------------------------{END}")
    display_info(memory)


if __name__ == "__main__":
    cli()