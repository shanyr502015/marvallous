import os

def main():
    print(os.cpu_count())  # 8, total number of CPU cores - 8, typically one CPU per laptop/desktop but with multiple cores

if __name__ == "__main__":
    main()

# Key points:
    # One CPU (physical chip) per laptop/desktop in most cases
    # Multiple cores within that single CPU (e.g., 4 cores, 8 cores, etc.)
    # os.cpu_count() returns the number of cores, not the number of CPUs

# is cpu and microprocessor are same or not?
    # Yes, CPU and microprocessor are essentially the same thing in modern context!
# Explanation:
    # CPU (Central Processing Unit): The brain of the computer that performs calculations and executes instructions
    # Microprocessor: A CPU implemented on a single integrated circuit (chip)

    # Historical context:
        # - In the early days of computing, CPUs were made of multiple large components
        # - When technology advanced, the entire CPU was integrated onto a single chip - this was called a "microprocessor"
        # - The first microprocessor was the Intel 4004 (1971)

    # Modern usage:
        # - Today, all CPUs are microprocessors (on a single chip)
        # - The terms are used interchangeably, When people say "CPU," they mean microprocessor
        # - Examples: Intel Core i7, AMD Ryzen 5, Apple M2 - all are microprocessors/CPUs

    # Simple answer: In today's world, CPU = Microprocessor. They're the same thing! The term "microprocessor" just emphasizes that it's a processor on a tiny chip.


# what "Intel Core i5" means ?
    # Intel Core i5 is a model/series name for Intel's mid-range processors (CPUs/microprocessors).
# Breaking it down:
    # 1. Intel = The company that made the processor (Intel Corporation)
    # 2. Core = The product family/brand name for consumer processors
    # 3. i5 = The performance tier within the Core family

# Intel's Core Series Hierarchy:**
    # - i3 = Basic/Entry-level (budget, everyday tasks)
    # - i5 = Mid-range (good balance of performance and price) ← Your laptop
    # - i7 = High-performance (power users, gaming, video editing)
    # - i9 = Extreme performance (professional workstations, heavy gaming)

# What it means for you:
    # - Your laptop has an Intel microprocessor** from the i5 series
    # - It's a mid-range CPU - good for multitasking, programming, moderate gaming, browsing, office work
    # - Likely has 4-8 cores depending on the generation

# Example full specification might be:
    # "Intel Core i5-12450H" where:
        # - i5 = series
        # - 12 = 12th generation
        # - 450H = specific model variant

# So that sticker is just telling you which CPU/microprocessor model is inside your laptop!