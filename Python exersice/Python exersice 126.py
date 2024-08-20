def all_sublists(lst):
    sublists = [[]]
    for start in range(len(lst)):
        for end in range(start + 1, len(lst) + 1):
            sublists.append(lst[start:end])
    return sublists

def main():
    example_lists = [
        [1, 2, 3],
        [4, 5],
        [1, 2, 3, 4, 5],
        []
    ]
    
    for lst in example_lists:
        print(f"All sublists of {lst}:")
        result = all_sublists(lst)
        for sublist in result:
            print(sublist)
        print()

main()
