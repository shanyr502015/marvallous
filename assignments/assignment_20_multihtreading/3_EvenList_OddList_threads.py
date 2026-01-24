import threading

def EvenList(numbers):
    print("\nEvenList thread started")
    even_elements = []
    # Extract all even elements
    for num in numbers:
        if num % 2 == 0:
            even_elements.append(num)

    # Display even elements
    print(f"Even elements: {even_elements}")
    # Calculate and display sum
    sum_even = sum(even_elements)
    print(f"Sum of even elements: {sum_even}")
    print("EvenList thread completed")

def OddList(numbers):
    print("\nOddList thread started")
    odd_elements = []
    # Extract all odd elements
    for num in numbers:
        if num % 2 != 0:
            odd_elements.append(num)
    
    # Display odd elements
    print(f"Odd elements: {odd_elements}")
    # Calculate and display sum
    sum_odd = sum(odd_elements)
    print(f"Sum of odd elements: {sum_odd}")
    print("OddList thread completed")

def main():
    # Get list of integers from user
    print("Enter integers separated by spaces:")
    user_input = input()
    numbers = list(map(int, user_input.split()))
    print(f"\nInput list: {numbers}")
    # Create two threads
    t1 = threading.Thread(target=EvenList, args=(numbers,))
    t2 = threading.Thread(target=OddList, args=(numbers,))
    # Start both threads
    t1.start()
    t2.start()
    # Wait for both threads to complete
    t1.join()
    t2.join()
    print("\nBoth threads completed execution")
if __name__ == "__main__":
    main()