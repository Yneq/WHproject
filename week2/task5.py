def find(spaces, stat, n):
    min_diff = float("inf")
    best_index = -1
    for index, (space, status) in enumerate(zip(spaces, stat)):
            if status == 1 and space == n:
                print(index)
                return index
            elif status == 1 and space > n:
                diff = space - n 
                if diff < min_diff:
                    min_diff = diff
                    best_index = index        
    if best_index != -1:
         print(best_index)
    else:
         print("-1")
         return -1

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2