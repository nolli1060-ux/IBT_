def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 3, 5])) 
print(find_duplicates([1, 2, 3]))            
print(find_duplicates([5, 5, 5]))           