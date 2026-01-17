import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


class DSU:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)  # 1-indexed

    def find(self, x):
        while self.parent[x] >= 0:
            if self.parent[self.parent[x]] >= 0:
                self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if -self.parent[a] < -self.parent[b]:
            a, b = b, a
        self.parent[a] += self.parent[b]
        self.parent[b] = a
        return True


def main():
    N, M = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    dsu = DSU(N)
    active = [False] * (N + 1)

    # add vertices from N -> 1
    comp = 0
    ans_add = [0] * (N + 1)  # ans_add[i] = #components after adding vertices i..N

    for v in range(N, 0, -1):
        active[v] = True
        comp += 1  # new isolated component appears

        for nei in g[v]:
            if active[nei]:
                if dsu.union(v, nei):
                    comp -= 1  # merged two components

        ans_add[v] = comp

    # We need: after deleting 1..i, which equals state with active vertices i+1..N
    # That's exactly ans_add[i+1]. For i=N => no vertices => 0.
    out = []
    for i in range(1, N + 1):
        if i == N:
            out.append("0")
        else:
            out.append(str(ans_add[i + 1]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
