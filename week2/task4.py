def get_number(index, numblist=[]):
    if not numblist:
        numblist.append(0)

    while len(numblist) <= index:
        if len(numblist) %3 == 0:
            nextnumb = numblist[-1] -1
        else: 
            nextnumb = numblist[-1] +4
        numblist.append(nextnumb)
    print(numblist[index])    
    return numblist[index]
    



get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25
get_number(30) # print 70