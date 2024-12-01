MOD = 1000000007

def calculate_sum(S):
    n = len(S)
    total_sum = 0
    current_sum = 0

    # Traverse the string
    for i in range(n):
        digit = int(S[i])

        # Update current_sum for the current digit
        current_sum = (current_sum * 10 + digit * (i + 1)) % MOD

        # Add current_sum to total_sum
        total_sum = (total_sum + current_sum) % MOD

    return total_sum

