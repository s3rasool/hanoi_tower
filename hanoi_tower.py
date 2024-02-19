def hanoi(from_pole, to_pole, help_pole, n, move_count):
    if n == 1:
        move_count[0] = move_count[0] + 1
        print(f"{move_count[0]} {from_pole} {to_pole}")
        return
    
    hanoi(from_pole, help_pole, to_pole, n-1, move_count)
    move_count[0] += 1
    print(f"{move_count[0]} {from_pole} {to_pole}")
    hanoi(help_pole, to_pole, from_pole, n-1, move_count)



n = int(input())
hanoi('A', 'B', 'C', n, [0])
