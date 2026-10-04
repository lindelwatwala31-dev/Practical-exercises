# Question 1.1
def distribute_n(n, k):
    if n <= k:
        return None
    result = [1] * k
    remainder = n - k
    for i in range(remainder):
        result[i % k] += 1
    return result

# Question 1.2
def pie_chart(percentages):
    if round(sum(percentages), 10) != 100:
        return None
    return [(p, (p / 100) * 360) for p in percentages]

# Question 1.3
def school_trip(n):
    taxi_capacity = 6
    num_taxis = -(-n // taxi_capacity)  # ceiling division
    result = []
    remaining = n
    for i in range(1, num_taxis + 1):
        students = min(taxi_capacity, remaining)
        result.append((f"taxi {i}:", students))
        remaining -= students
    return result