import heapq

def minimized_cable_connection(list_length_cable):
    heapq.heapify(list_length_cable)
    total_cost = 0

    while len(list_length_cable) > 1:
        first_min = heapq.heappop(list_length_cable)
        second_min = heapq.heappop(list_length_cable)
        cables_sum = first_min + second_min
        total_cost += cables_sum
        heapq.heappush(list_length_cable, cables_sum)
    return total_cost

cables = [2,6,10,8,1]
result = minimized_cable_connection(cables)
print(f"\nMinimum cost of connecting cables: {result}")