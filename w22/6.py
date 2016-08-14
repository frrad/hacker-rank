n = int(raw_input())

memo = {'': -1}


def hashable(state):
    return ''.join(map(str, state))


state = []
header = -1
for i in xrange(n):
    diff = raw_input().split()
    if diff[0] == '-':
        state.pop()
        header = memo[hashable(state)]
    else:
        new_number = int(diff[1])
        state.append(new_number)
        if header > -1 and new_number != state[len(state) - header - 1]:
            header = -1

        if header == -1:
            if len(state) > 1 and new_number == state[0]:
                header = len(state) - 1

        memo[hashable(state)] = header

    if header == -1:
        print 0
    else:
        print len(state) - header
