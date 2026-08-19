# =========================================================
#  여기서부터 5개 함수만 구현하시오.
#  (파이썬 내장과의 충돌을 피하기 위해 함수명은 아래 이름을 그대로 사용한다)
#  main 및 입출력 부분은 수정하지 않는 것을 권장한다.
#
#  init       : 각 테스트 케이스 시작 시 1회 호출. 전역 자료 구조 초기화.
#  add_stress : 구간 [l,r] 의 모든 구간 피로도를 w 만큼 증가(range add).
#  repair     : 구간 [l,r] 을 v 로 재설정(range assign, v=0 가능).
#  get_peak   : 구간 [l,r] 의 최대 피로도 반환(range max).
#  find_risk  : 구간 [l,r] 에서 값 >= x 인 가장 왼쪽 인덱스 반환, 없으면 -1.
# =========================================================

def init(N, fatigue):
    global n, tree, lazy_add, lazy_set
    global _push, _apply_add, _apply_set

    n = N
    if N == 0:
        tree = [0]
        lazy_add = [0]
        lazy_set = [None]

        def apply_set(node, value):
            return

        def apply_add(node, value):
            return

        def push(node):
            return

        _apply_set = apply_set
        _apply_add = apply_add
        _push = push
        return

    size = 1 << (N - 1).bit_length()
    tree_size = size * 2

    tree = [0] * tree_size
    lazy_add = [0] * tree_size
    lazy_set = [None] * tree_size

    def apply_set(node, value):
        tree[node] = value
        lazy_set[node] = value
        lazy_add[node] = 0

    def apply_add(node, value):
        tree[node] += value

        # 이미 set이 예약되어 있다면
        # set 값 자체에 add를 합칠 수 있음
        if lazy_set[node] is not None:
            lazy_set[node] += value
        else:
            lazy_add[node] += value

    def push(node):
        # set을 먼저 전달
        if lazy_set[node] is not None:
            value = lazy_set[node]

            apply_set(node * 2, value)
            apply_set(node * 2 + 1, value)

            lazy_set[node] = None

        # 그 다음 add 전달
        if lazy_add[node] != 0:
            value = lazy_add[node]

            apply_add(node * 2, value)
            apply_add(node * 2 + 1, value)

            lazy_add[node] = 0

    _apply_set = apply_set
    _apply_add = apply_add
    _push = push

    def build(node, start, end):
        if start == end:
            tree[node] = fatigue[start]
            return

        mid = (start + end) // 2

        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)

        tree[node] = max(
            tree[node * 2],
            tree[node * 2 + 1]
        )

    build(1, 0, N - 1)


def add_stress(l, r, w):
    def update(node, start, end):
        # 겹치지 않음
        if end < l or r < start:
            return

        # 현재 구간 전체가 [l, r] 안에 포함
        if l <= start and end <= r:
            _apply_add(node, w)
            return

        _push(node)

        mid = (start + end) // 2

        update(node * 2, start, mid)
        update(node * 2 + 1, mid + 1, end)

        tree[node] = max(
            tree[node * 2],
            tree[node * 2 + 1]
        )

    update(1, 0, n - 1)


def repair(l, r, v):
    def update(node, start, end):
        # 겹치지 않음
        if end < l or r < start:
            return

        # 현재 구간 전체가 [l, r] 안에 포함
        if l <= start and end <= r:
            _apply_set(node, v)
            return

        _push(node)

        mid = (start + end) // 2

        update(node * 2, start, mid)
        update(node * 2 + 1, mid + 1, end)

        tree[node] = max(
            tree[node * 2],
            tree[node * 2 + 1]
        )

    update(1, 0, n - 1)


def get_peak(l, r):
    def query(node, start, end):
        # 범위 밖
        if end < l or r < start:
            return -float('inf')

        # 완전히 포함됨
        if l <= start and end <= r:
            return tree[node]

        _push(node)

        mid = (start + end) // 2

        left_max = query(node * 2, start, mid)
        right_max = query(node * 2 + 1, mid + 1, end)

        return max(left_max, right_max)

    return query(1, 0, n - 1)


def find_risk(l, r, x):
    def search(node, start, end):
        # [l, r]과 겹치지 않음
        if end < l or r < start:
            return -1

        # 이 node의 최댓값조차 x보다 작음
        # -> 이 subtree에는 정답 없음
        if tree[node] < x:
            return -1

        # 여기까지 왔는데 leaf라면
        # 해당 값은 반드시 x 이상
        if start == end:
            return start

        _push(node)

        mid = (start + end) // 2

        # 가장 작은 index가 필요하므로 왼쪽부터
        result = search(node * 2, start, mid)

        if result != -1:
            return result

        return search(node * 2 + 1, mid + 1, end)

    return search(1, 0, n - 1)


def main():
    T = int(input())
    final_output = []

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        fatigue = list(map(int, input().split()))
        init(N, fatigue)

        case_output = [f"#{test_case}"]

        for _ in range(M):
            task = list(map(int, input().split()))
            cmd = task[0]

            if cmd == 1:
                add_stress(task[1], task[2], task[3])
            elif cmd == 2:
                repair(task[1], task[2], task[3])
            elif cmd == 3:
                case_output.append(str(get_peak(task[1], task[2])))
            elif cmd == 4:
                case_output.append(str(find_risk(task[1], task[2], task[3])))

        final_output.append("\n".join(case_output))

    print("\n".join(final_output))


main()