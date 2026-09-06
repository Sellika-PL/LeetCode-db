class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:

        paths.sort(key=len)
        shortest_length = len(paths[0])

        MOD1 = 1_000_000_007
        MOD2 = 1_000_000_009
        BASE = 100_000

        # Precompute powers
        power1 = [1] * (shortest_length + 1)
        power2 = [1] * (shortest_length + 1)

        for i in range(1, shortest_length + 1):
            power1[i] = (power1[i - 1] * BASE) % MOD1
            power2[i] = (power2[i - 1] * BASE) % MOD2


        def get_hashes(path, length):
            prefix1 = [0] * (len(path) + 1)
            prefix2 = [0] * (len(path) + 1)

            for i, num in enumerate(path):
                prefix1[i + 1] = (prefix1[i] * BASE + num + 1) % MOD1
                prefix2[i + 1] = (prefix2[i] * BASE + num + 1) % MOD2

            hashes = set()

            for i in range(len(path) - length + 1):
                h1 = (
                    prefix1[i + length]
                    - prefix1[i] * power1[length]
                ) % MOD1

                h2 = (
                    prefix2[i + length]
                    - prefix2[i] * power2[length]
                ) % MOD2

                hashes.add((h1, h2))

            return hashes


        def possible(length):
            if length == 0:
                return True

            common = get_hashes(paths[0], length)

            for path in paths[1:]:
                current = get_hashes(path, length)
                common &= current

                if not common:
                    return False

            return True


        left = 0
        right = shortest_length

        while left < right:
            mid = (left + right + 1) // 2

            if possible(mid):
                left = mid
            else:
                right = mid - 1

        return left
        