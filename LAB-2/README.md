```python
def merge_sort_iterative(a):
  
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    
    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
           
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            j += 2 * i
            
        i *= 2
        
    return a, comparisons, assignments

def merge(a, left, mid, right):
    
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
 
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2
    
    it1 = 0
    it2 = 0
    k = left
    assignments += 3 # присвоєння it1, it2, k

    while it1 < n1 and it2 < n2:
        comparisons += 1
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        assignments += 2 # запис в a[k] та інкремент ітератора
        k += 1
        assignments += 1

    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 3
        
    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 3
        
    return comparisons, assignments

if __name__ == "__main__":
    input_sequence = [69, 52, 97, 27, 10, 88, 29, 1, 24]
    print("=== Сортування злиттям ===")
    
    seq_merge = input_sequence.copy()
    print("Вхідний масив:", seq_merge)
    
    sorted_merge, comps_merge, assigs_merge = merge_sort_iterative(seq_merge)
    
    print("Відсортований масив:", sorted_merge)
    print(f"Кількість порівнянь: {comps_merge}")
    print(f"Кількість присвоювань: {assigs_merge}")
```

```python
def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    
    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1
        
        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else:
        return 0, 0, 0
        
    return comparisons, assignments, recursive_calls


def partition(a, l, r):
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    
    i = l - 1
    j = r + 1
    assignments += 2
    
    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1
        
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1
        
        comparisons += 1
        if i >= j:
            return j, comparisons, assignments
            
        a[i], a[j] = a[j], a[i]
        assignments += 3


if __name__ == "__main__":
    input_sequence = [69, 52, 97, 27, 10, 88, 29, 1, 24]
    print("=== Швидке сортування ===")
    
    seq_quick = input_sequence.copy()
    print("Вхідний масив:", seq_quick)
    
    comps_quick, assigs_quick, calls_quick = quicksort(seq_quick, 0, len(seq_quick) - 1)
    
    print("Відсортований масив:", seq_quick)
    print(f"Кількість порівнянь: {comps_quick}")
    print(f"Кількість присвоювань: {assigs_quick}")
    print(f"Кількість рекурсивних викликів: {calls_quick}")

```
