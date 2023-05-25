def counting_sort(original, k):
  counter_list = [0] * (k + 1)
  original_length = len(original)

  for i in range(original_length):
    counter_list[original[i]] += 1

  result = [-1] * (original_length)

  for j in range(1, k + 1):
    counter_list[j] += counter_list[j - 1]

  for k in range(original_length - 1, -1, -1):
    counter_list[original[k]] -= 1
    result[counter_list[original[k]]] = original[k]

  return result


a = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(a, 4))  # [0, 1, 1, 1, 2, 3, 4, 4]