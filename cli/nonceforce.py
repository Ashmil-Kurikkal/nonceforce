"""
Title: DSA Nonce Brute-Forcer (CPU Multiprocessing)
Author: k3yb0ard/Ashmil Kurikkal
Date: 23-03-2025

Description:
This script utilizes CPU multiprocessing to brute-force the nonce (k) used in the DSA signature scheme.
It exploits weaknesses in nonce generation to recover the private key (priv) and retrieve the signed message.
By leveraging multiple CPU cores, the script significantly speeds up the brute-force process.

Features:
- Uses Python's multiprocessing module for parallel computation.
- Dynamically allocates CPU cores for efficient processing.
- Designed for scenarios where GPU acceleration is unavailable.

Requirements:
- Python 3.x
- Multiprocessing module (built into Python)
- PyCryptodome or hashlib for SHA-256 operations

Usage:
- Ensure your system has multiple CPU cores available.
- Adjust the process count based on your CPU capabilities (default is maximum cores).
- Provide the known r, s, message hash, and DSA parameters.
- The script will distribute nonce (k) values across multiple processes for efficient brute-forcing.

Performance Considerations:
- High CPU utilization is expected. Running at 100% may cause thermal throttling if cooling is inadequate.
- To limit CPU load, adjust the number of worker processes.
- Running on a high-performance CPU will improve speed. Intel i7-12650H was used for testing and completed in under a minute.

Disclaimer:
This script is intended for educational and ethical hacking purposes only.
Unauthorized use against real-world systems is strictly prohibited.

"""

import hashlib
import multiprocessing
import sys
import time
from colorama import Fore, Back, Style, init
from pyfiglet import Figlet


init(autoreset=True)


def typewriter(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")


def check_nonce(k, p, q, g, r, s, hashed_message):
    """Checks if the given nonce k produces the expected r value and derives the private key if valid."""
    r_check = pow(g, k, p) % q
    if r_check == r:
        priv_key = ((s * k - hashed_message) * pow(r, -1, q)) % q
        return k, priv_key
    return None


def brute_force_range(k_range, p, q, g, r, s, hashed_message, result_queue):
    for k in k_range:
        result = check_nonce(k, p, q, g, r, s, hashed_message)
        if result:
            result_queue.put(result)
            return

def parallel_brute_force(k_min, k_max, p, q, g, r, s, hashed_message):
    cpu_count = multiprocessing.cpu_count()
    print(f"\nUsing {cpu_count} CPU cores for brute-force...")


    result_queue = multiprocessing.Queue()


    step = (k_max - k_min) // cpu_count
    ranges = [(range(k_min + i * step, k_min + (i + 1) * step), p, q, g, r, s, hashed_message, result_queue) for i in range(cpu_count)]

    processes = [multiprocessing.Process(target=brute_force_range, args=args) for args in ranges]
    for process in processes:
        process.start()


    found = None
    while found is None:
        try:
            found = result_queue.get(timeout=1)  
        except:
            if all(not p.is_alive() for p in processes):
                break


    for process in processes:
        process.terminate()
        process.join()

    if found:
        k, priv_key = found
        print(f"\n{Fore.GREEN}[+] Found nonce value or k: {k}")
        print(f"{Fore.GREEN}[+] Possible Private Key: {priv_key}")
    else:
        print(f"\n{Fore.RED}[-] No valid k found in the given range.")

if __name__ == "__main__":

    f = Figlet(font="slant")
    print("-" * 80)
    typewriter(f.renderText("k3yb0ard"), delay=0.002)
    print(" " * 50 + Fore.BLACK + Back.LIGHTGREEN_EX + "Nonce Brute-Forcer")
    print(" " * 50 + Fore.BLACK + Back.GREEN + "CPU Multiprocessing")
    typewriter("Digital Signature Algorithm (DSA)")
    print("-" * 80 + "\n")

  
    p = int(input("Enter the known value of 'p': "))
    q = int(input("Enter the known value of 'q': "))
    g = int(input("Enter the known value of 'g': "))
    
    print("\nSignatures:")
    r = int(input("r: "))
    s = int(input("s: "))


    m = input("Enter the message hash value: ")
    hashed_message = int(m, 16) 

    print()
    k_min = int(input("Enter the starting value of k: "))
    k_max = int(input("Enter the ending value of k: "))


    parallel_brute_force(k_min, k_max, p, q, g, r, s, hashed_message)
