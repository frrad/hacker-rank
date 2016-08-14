n = int(raw_input())


def solve(state):
    if len(state) == 0:
        return 0
    for i in xrange(len(state) - 1, -1, -1):
        if equals(state[:i], state[-i:]):
            return i


def equals(a, b):
    for x, y in zip(a, b):
        if x != y:
            return False
    return True

state = []
for i in xrange(n):
    inputs = raw_input().strip().split()
    if inputs[0] == '-':
        state.pop()
    else:
        state.append(inputs[1])
    print solve(state)
