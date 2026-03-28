def list_sum(lst):
    return sum(lst)

arr = list(map(int, input("Enter elements: ").split()))
print(list_sum(arr))