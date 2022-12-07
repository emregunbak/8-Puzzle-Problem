# Depth first search in search of target - Using Recursion
def dfs(src, target, limit, visited_states):
    # Base case if Target found
    if src == target:
        return True

    # Base case if limit exceeded
    if limit <= 0:
        return False

    # Add source to visited_states
    visited_states.append(src)

    # Find possible slides up, down, left right to current empty site
    possible_moves_list = possible_moves(src, visited_states)

    for i in possible_moves_list:
        if dfs(i, target, limit - 1, visited_states):
            return True

    return False


def possible_moves(state, visited_states):
    # Find index of empty spot
    b = state.index(-1)

    # 'd' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    d = ["d", "u", "r", "l"]

    # Removes directions that are not possible
    if b % 3 == 0:
        d.remove("l")
    if b % 3 == 2:
        d.remove("r")
    if b in range(0, 3):
        d.remove("u")
    if b in range(6, 9):
        d.remove("d")

    pos_moves = []

    # for all possible directions find the state if that move is played
    for m in d:
        move = gen(state, m, b)
        if move not in visited_states:
            pos_moves.append(move)

    # return all possible moves only if the move not in visited_states
    return pos_moves


def gen(state, m, b):  # m(move) is direction to slide, b(blank) is index of empty spot
    # create a copy of current state to test the move
    temp = state.copy()

    if m == "l":  # left
        temp[b] = temp[b - 1]
        temp[b - 1] = state[b]

    elif m == "r":  # right
        temp[b] = temp[b + 1]
        temp[b + 1] = state[b]

    elif m == "u":  # up
        temp[b] = temp[b - 3]
        temp[b - 3] = state[b]

    elif m == "d":  # down
        temp[b] = temp[b + 3]
        temp[b + 3] = state[b]

    else:
        print("direction is not valid")

    return temp


def ids(src, target, depth):
    # iterative-deepening search
    return dfs(src, target, depth, [])


# Test 1
src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]

depth = 1
print("Test-1: ", ids(src, target, depth))  # Minimum depth should be 2

# Test 2
src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 6, 4, 5, -1, 7, 8]

depth = 1
print("Test-2: ", ids(src, target, depth))  # Minimum depth is 1
