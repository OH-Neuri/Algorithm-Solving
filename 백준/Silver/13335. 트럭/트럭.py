from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

bridge = deque(bridge)
trucks = deque(trucks)
while bridge:
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

print(time)