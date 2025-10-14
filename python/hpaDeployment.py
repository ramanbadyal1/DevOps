import math
import time
import sys

def stress_cpu(duration):
    """
    Runs an infinite loop performing a dummy calculation to stress the CPU
    for a specified duration in seconds.
    """
    start_time = time.time()
    print(f"Starting CPU stress test for {duration} seconds...")
    while time.time() - start_time < duration:
        _ = math.sqrt(math.pi * math.pi) * math.log(math.e) * math.factorial(100) / 99
        pass
    print(f"CPU stress test finished after {duration} seconds.")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            duration = int(sys.argv[1])
        else:
            duration = 3600 
    except ValueError:
        print("Invalid duration provided. Usage: python3 cpu_stress.py [seconds]")
        sys.exit(1)
        
    stress_cpu(duration)
