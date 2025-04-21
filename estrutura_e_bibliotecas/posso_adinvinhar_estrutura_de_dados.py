import sys
import heapq
from collections import deque

for linha in sys.stdin:
    try:
        n = int(linha)
        stack = []
        queue = deque()
        pqueue = []
        is_stack = True
        is_queue = True
        is_pqueue = True

        for _ in range(n):
            comando = input().strip().split()
            tipo = int(comando[0])
            x = int(comando[1])

            if tipo == 1:
                stack.append(x)
                queue.append(x)
                heapq.heappush(pqueue, -x)  # Usamos valores negativos para simular max-heap
            else:
                if is_stack:
                    if not stack or stack.pop() != x:
                        is_stack = False
                if is_queue:
                    if not queue or queue.popleft() != x:
                        is_queue = False
                if is_pqueue:
                    if not pqueue or -heapq.heappop(pqueue) != x:
                        is_pqueue = False

        total_true = sum([is_stack, is_queue, is_pqueue])
        if total_true > 1:
            print("not sure")
        elif total_true == 1:
            if is_stack:
                print("stack")
            elif is_queue:
                print("queue")
            else:
                print("priority queue")
        else:
            print("impossible")
    except EOFError:
        break
