import threading

def EvenFactor(no):
    even_factors = []
    # Find all factors
    for i in range(1, no + 1):
        if no % i == 0:  # i is a factor
            if i % 2 == 0:  # i is even
                even_factors.append(i)
    
    # Display even factors
    print(f"Even factors of {no}: {even_factors}")
    # Calculate and display sum
    sum_even = sum(even_factors)
    print(f"Sum of even factors: {sum_even}")
    print("EvenFactor thread completed")


def OddFactor(no):
    odd_factors = []
    # Find all factors
    for i in range(1, no + 1):
        if no % i == 0:  # i is a factor
            if i % 2 != 0:  # i is odd
                odd_factors.append(i)
    
    # Display odd factors
    print(f"Odd factors of {no}: {odd_factors}")
    # Calculate and display sum
    sum_odd = sum(odd_factors)
    print(f"Sum of odd factors: {sum_odd}")
    print("OddFactor thread completed")

def main():
    # Get input from user
    number = int(input("Enter a number: "))
    # Create two threads
    t1 = threading.Thread(target=EvenFactor, args=(number,))
    t2 = threading.Thread(target=OddFactor, args=(number,))
    # Start both threads
    t1.start()
    t2.start()
    # Wait for both threads to complete
    t1.join()
    t2.join()
    # Display exit message
    print("\nExit from main")
if __name__ == "__main__":
    main()