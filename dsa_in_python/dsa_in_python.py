# Why Learn Data Structures?
    # Data structures are fundamental to software development and are used extensively in everyday applications like web browsers, Google Maps, music players, and booking systems. 
    # Understanding them helps you build efficient, scalable applications.

# 1. Arrays (Lists in Python)
# Concept: Arrays store elements in contiguous memory locations with index-based access.
# Real-Life Example: Online Ticket Booking System: Theater seats arranged in rows and columns represent a 2D array. A seat at row 3, column 4 is accessed as `seats[3][4]`.
# Python Implementation
# 1D Array (List)
seats_row = ['A1', 'A2', 'A3', 'A4', 'A5']
print(seats_row[2])  # Access 3rd seat: 'A3'
# 2D Array (Theater Seating)
theater = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'C2', 'C3']
]
print(theater[2][1])  # Row 3, Column 2: 'C2'
# Booking a seat
def book_seat(theater, row, col):
    if theater[row][col] != 'Booked':
        theater[row][col] = 'Booked'
        return True
    return False
# Key Operations
    # - Access: O(1)
    # - Search: O(n)
    # - Insert/Delete: O(n)

# 2. Stack (LIFO - Last In First Out)
# Concept: Elements are added and removed from the same end (top). Like a stack of plates.
# Real-Life Example: Browser History: Each visited webpage is pushed onto a stack. Clicking "Back" pops the last visited page.
# Python Implementation
class BrowserHistory:
    def __init__(self):
        self.history = []
    def visit(self, url):
        self.history.append(url)
        print(f"Visited: {url}")
    def back(self):
        if len(self.history) > 1:
            self.history.pop()
            current = self.history[-1]
            print(f"Back to: {current}")
            return current
        print("No previous page")
        return None
# Usage
browser = BrowserHistory()
browser.visit("www.google.com")
browser.visit("log2base2.com")
browser.visit("www.youtube.com")
browser.back()  # Returns to log2base2.com
browser.back()  # Returns to www.google.com
# Using Python's Built-in
stack = []
stack.append('google.com')  # Push
stack.append('youtube.com')
stack.pop()  # Pop - returns 'youtube.com'
# Key Operations
    # - Push: O(1)
    # - Pop: O(1)
    # - Peek: O(1)

# 3. Queue (FIFO - First In First Out)
# Concept: Elements are added at the rear and removed from the front. Like a line at a bank.
# Real-Life Example: Bank Queue: First customer in line gets served first.
# Python Implementation
from collections import deque
class BankQueue:
    def __init__(self):
        self.queue = deque()
    def add_customer(self, name):
        self.queue.append(name)
        print(f"{name} joined the queue")
    def serve_customer(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"Serving: {customer}")
            return customer
        print("Queue is empty")
        return None
# Usage
bank = BankQueue()
bank.add_customer("Alice")
bank.add_customer("Bob")
bank.add_customer("Charlie")
bank.serve_customer()  # Serves Alice
bank.serve_customer()  # Serves Bob
# Key Operations
    # - Enqueue: O(1)
    # - Dequeue: O(1)

# 4. Linked Lists
# Concept: Elements (nodes) are connected through pointers/references, allowing dynamic size.

# 4a. Singly Linked List

# Real-Life Example: Music Player (Basic): Songs play sequentially. You can go to the next song but not back.
# Python Implementation
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
class MusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None
    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.current = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Now playing: {self.current.song}")
        else:
            print("End of playlist")
# Usage
player = MusicPlayer()
player.add_song("Song 1")
player.add_song("Song 2")
player.add_song("Song 3")
print(f"Playing: {player.current.song}")
player.play_next()
player.play_next()

# 4b. Doubly Linked List

# Real-Life Example: Music Player (Advanced): Navigate both forward (next) and backward (previous).
# Python Implementation
class DoublyNode:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
class AdvancedMusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None
    def add_song(self, song):
        new_node = DoublyNode(song)
        if not self.head:
            self.head = new_node
            self.current = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Next: {self.current.song}")
    def play_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Previous: {self.current.song}")
# Usage
player = AdvancedMusicPlayer()
player.add_song("Song 1")
player.add_song("Song 2")
player.add_song("Song 3")
player.play_next()
player.play_next()
player.play_previous()  # Goes back to Song 2

# 4c. Circular Linked List

# Real-Life Example: Music Player (Repeat Mode): After the last song, playlist loops back to the first song.
# Python Implementation
class CircularNode:
    def __init__(self, song):
        self.song = song
        self.next = None
class RepeatMusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None
    def add_song(self, song):
        new_node = CircularNode(song)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
            self.current = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Complete the circle
    def play_next(self):
        if self.current:
            self.current = self.current.next
            print(f"Playing: {self.current.song}")
# Usage
player = RepeatMusicPlayer()
player.add_song("Song 1")
player.add_song("Song 2")
player.add_song("Song 3")
player.play_next()  # Song 2
player.play_next()  # Song 3
player.play_next()  # Song 1 (loops back)

# Key Operations
    # - Access: O(n)
    # - Insert at beginning: O(1)
    # - Insert at end: O(n) or O(1) with tail pointer
    # - Delete: O(n)


# 5. Graphs
# Concept: Collection of nodes (vertices) connected by edges. Can be directed or undirected, weighted or unweighted.
# Real-Life Example: Google Maps: Cities are nodes, roads are edges with distances. Algorithms find the shortest path.
# Python Implementation
from collections import defaultdict, deque
import heapq
class CityMap:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_road(self, city1, city2, distance):
        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))  # Undirected
    def shortest_path(self, start, end):
        # Dijkstra's Algorithm
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        previous = {}
        while pq:
            current_dist, current = heapq.heappop(pq)
            if current == end:
                break
            if current_dist > distances[current]:
                continue
            for neighbor, weight in self.graph[current]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        # Reconstruct path
        path = []
        current = end
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
        return path, distances[end]
# Usage
map_system = CityMap()
map_system.add_road("Tamil Nadu", "Karnataka", 500)
map_system.add_road("Karnataka", "Maharashtra", 400)
map_system.add_road("Maharashtra", "Delhi", 600)
map_system.add_road("Tamil Nadu", "Maharashtra", 1500)
path, distance = map_system.shortest_path("Tamil Nadu", "Delhi")
print(f"Shortest path: {' -> '.join(path)}")
print(f"Total distance: {distance} km")
# Key Graph Algorithms
    # - BFS (Breadth-First Search): O(V + E)
    # - DFS (Depth-First Search): O(V + E)
    # - Dijkstra's Algorithm: O((V + E) log V)

# Summary Table
# ---------------------------------------------------------------------------------------------------------
# | Data Structure       | Real-Life Example        | Time Complexity     | Python Implementation         |
# |----------------------|--------------------------|---------------------|-------------------------------|
# | Array                | Ticket Booking           | Access: O(1)        | `list[]`                      |
# | Stack                | Browser History          | Push/Pop: O(1)      | `list.append()`, `list.pop()` |
# | Queue | Bank Line    | Enqueue/Dequeue: O(1)    | `collections.deque` |
# | Singly Linked List   | Music Player             | Access: O(n)        | Custom class                  |
# | Doubly Linked List   | Music Player (prev/next) | Access: O(n)        | Custom class                  |
# | Circular Linked List | Repeat Playlist          | Access: O(n)        | Custom class                  |
# | Graph                | Google Maps              | Varies by algorithm | `defaultdict(list)`           |
# ---------------------------------------------------------------------------------------------------------

# When to Use Each Structure
    # Arrays: Fixed-size collections, frequent random access, matrix operations
    # Stack: Undo/redo, expression evaluation, backtracking, function calls
    # Queue: Task scheduling, breadth-first search, printer queue
    # Linked List: Dynamic size, frequent insertions/deletions, implementing stacks/queues
    # Graph: Networks, social connections, maps, dependencies