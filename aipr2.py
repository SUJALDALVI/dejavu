import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def print_puzzle(state):
    print()
    for row in state:
        print("|", end=" ")
        for val in row:
            print(val if val != 0 else "_", end=" | ")
        print()
    print()


def heuristic(state):
    # misplaced tiles
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def a_star(start):
    pq = []
    visited = set()
    counter = 0   # tie-breaker

    heapq.heappush(pq, (0, counter, start, []))

    while pq:
        cost, _, state, path = heapq.heappop(pq)

        state_key = state_to_tuple(state)
        if state_key in visited:
            continue

        visited.add(state_key)
        path = path + [state]

        if state == goal:
            print("\nGOAL REACHED!\n")
            print("Solution Path:\n")
            for step in path:
                print_puzzle(step)
            return

        x, y = find_blank(state)

        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                new_key = state_to_tuple(new_state)

                if new_key not in visited:
                    g = len(path)
                    h = heuristic(new_state)
                    counter += 1
                    heapq.heappush(pq, (g+h, counter, new_state, path))


# START STATE
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

print("\nSTART STATE:\n")
print_puzzle(start)

a_star(start)