class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:

        def z_function(text):
            n = len(text)
            z = [0] * n
            left = right = 0

            for i in range(1, n):
                if i <= right:
                    z[i] = min(right - i + 1, z[i - left])

                while i + z[i] < n and text[z[i]] == text[i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > right:
                    left = i
                    right = i + z[i] - 1

            return z

        # Matching prefix lengths
        z1 = z_function(pattern + "#" + s)

        # Matching suffix lengths
        rev_pattern = pattern[::-1]
        rev_s = s[::-1]
        z2 = z_function(rev_pattern + "#" + rev_s)

        n = len(s)
        m = len(pattern)

        for i in range(n - m + 1):

            # Characters matching from the beginning
            prefix = min(z1[m + 1 + i], m)

            if prefix == m:
                return i

            # Characters matching from the end
            reverse_index = n - (i + m)
            suffix = min(z2[m + 1 + reverse_index], m)

            # prefix + suffix covers all except at most one character
            if prefix + suffix >= m - 1:
                return i

        return -1
        