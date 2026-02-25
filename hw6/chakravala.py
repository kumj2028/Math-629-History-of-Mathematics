import math

def chakravala(x, y, k, n, steps=1000):
    for _ in range(steps):
        if k == 1:
            return (x, y, k)
        m = minimize_m(x, y, k, n)
        x1 = (m * x + n * y) // abs(k)
        y1 = (x + m * y) // abs(k)
        k1 = (m * m - n) // k
        print(f"x: {x}, y: {y}, k: {k}, m: {m}, x1: {x1}, y1: {y1}, k1: {k1}")
        x, y, k = x1, y1, k1
    raise RuntimeError("Did not converge within step limit")

def minimize_m(x, y, k, n, search_radius=10000):
    # Search m near sqrt(n), in both directions, among values satisfying congruence conditions
    root = int(math.isqrt(n))
    best_m = None
    min_diff = float('inf')

    # search around sqrt(n): root, root+1, root-1, root+2, root-2, ...
    for d in range(search_radius + 1):
        candidates = [root + d, root - d] if (root - d) > 0 else [root + d]
        for m in candidates:
            # Divisibility conditions matching x1, y1, k1
            if (x + m * y) % abs(k) == 0 :
                diff = abs(m * m - n)
                if diff < min_diff:
                    min_diff = diff
                    best_m = m
                    print(f"m: {m}, m^2: {m*m}, diff: {diff}")

                # Since we're searching outward from sqrt(n), first valid one is usually optimal
                # Uncomment next line if you want the first valid nearest-to-sqrt(n) choice:
                # return m

    if best_m is None:
        raise ValueError("No valid m found in search range")
    return best_m

if __name__ == "__main__":
    print("Enter x, y, k, n separated by commas:")
    x, y, k, n = map(int, input().split(','))
    print(chakravala(x, y, k, n))