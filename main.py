from copy import deepcopy
from collections import deque, Counter

max_inventory = 22
start = Counter({
    'a': 0,
    'b': 3,
    'c': 2,
    'd': 5,
    'e': 6
})

end = Counter({
    'a': 2,
    'b': 3,
    'c': 1,
    'd': 5,
    'e': 6
})

states = [
    Counter({'a': 2, 'c': -1}),
    Counter({'a': -2, 'c': -2, 'd': 2, 'e': 2}),
    Counter({'a': 3, 'b': -2, 'd': -1, 'e': 1}),
    Counter({'a': 2, 'b': -1, 'c': -1, 'e': 2}),
]

for i in start.keys():
    for j in start.keys():
        if i != j:
            states.append(Counter({i: -3, j: 1}))

stack = deque([(start, [])])
previous = set()

while(len(stack)):
    current, path = stack.pop()
    for state in states:
        tmp = deepcopy(current)
        tmp.update(state)

        if sum(tmp.values()) > max_inventory:
            continue
        
        if not all(value >= 0 for key, value in tmp.items()):
            continue
        
        if hash(frozenset(sorted(tmp.items()))) in previous:
            continue
    
        if all(tmp[key] >= value for key, value in end.items()):
            print('success')
            print(tmp)
            print(path + [state])
        
        if sum(1 if tmp[key] - value >= 0 else 0 for key, value in end.items()) > 4:
            print(tmp)
        previous.add(hash(frozenset(sorted(tmp.items()))))
        stack.append((tmp, path + [state]))
        if len(path + [state]) > 15:
            print(tmp)
            print(path + [state])
