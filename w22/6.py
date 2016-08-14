n = int(raw_input())
memo = [[]]


def update(state, headers):
    new_number = state[-1]
    if new_number == state[0] and len(state) > 1:
        headers.append(len(state) - 1)
    kill_list = []
    for index in headers:
        if new_number != state[len(state) - index - 1]:
            kill_list.append(index)
    for kill in kill_list:
        headers.remove(kill)
    # finally, update our table with a copy
    memo.append(list(headers))


def lookup(state):
    return list(memo[''.join(map(str, state))])

state = []
headers = []
for i in xrange(n):
    diff = raw_input().split()
    if diff[0] == '-':
        state.pop()
        memo.pop()
        headers = list(memo[-1])
    else:
        state.append(int(diff[1]))
        update(state, headers)
    if len(headers) == 0:
        print 0
    else:
        print len(state) - min(headers)
