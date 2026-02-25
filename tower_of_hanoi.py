def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move source", source, "to destination", destination)
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("move disk", n-1, "from source", source, "to destination", destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
