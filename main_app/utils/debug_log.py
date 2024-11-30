from colorama import Fore, Style
# import os 

# DEBUG_MODE = os.getenv("DEBUG")

# def set_debug_mode(enabled):
#     global DEBUG_MODE
#     DEBUG_MODE = enabled

def error(message):
    print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}")
    
def success(message):
    print(f"{Fore.GREEN}[SUCCESS] {message}{Style.RESET_ALL}")

def warning(message):
    print(f"{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}")

def info(message):
    print(f"{Fore.BLUE}[INFO] {message}{Style.RESET_ALL}")