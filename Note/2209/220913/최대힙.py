

def enq(n):
    global last
    last += 1               # 마지막 정점 추가
    heap[last] = n          # 마지막 정점에 key 추가

    c = last
    p = c//2                # 완전 이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:
        # 부모 < 자식인 경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1]           # 루트 백업
    # 삭제할 노드의 키를 루트에 복사
    heap[1] = heap[last]    # 마지막 것을 heap로 옮겨 담기
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p*2                 # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1          # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로 교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c           # 조금 전의 자식을 새로운 부모로 변경
            c = p*2         # 왼쪽 자식 번호를 계산
        else:               # 부모가 더 크면
            break           #  비교 중단.
    return tmp

    # p 를 넣는 이유는 0 의 값일 경우 멈추도록 하기 위해서.

# 최대 힙
heap = [0]*100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
# print(heap)
while last:
    print(deq())