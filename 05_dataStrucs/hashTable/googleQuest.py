def n_repetido(array):
    nums = {}
    for i in range(0, len(array)):
        if array[i] in nums:
            return array[i]
        nums[array[i]]= i
    return None


print(n_repetido([1,2,36,5,36,31,2,36,51]))
print(n_repetido([5,1,2,3,51,2,23,44]))
print(n_repetido([51,2,23,44]))
print(n_repetido([31,2,36,51,23,44]))
print(n_repetido([2,36,31,2,36,51,23,]))
print(n_repetido([7,435,8,34,773,36,31]))
print(n_repetido([36,51,8,34,773,36,51,23]))
print(n_repetido([36,511,2,36,5,36,31]))