def generate_even_numbers():
    n = 0
    while True:
        yield n
        n += 4
        yield n
        n += 4
        yield n
        n += 1
def get_nth_numbers(n):
    counter = 1 
    for number in generate_even_numbers():
        if counter == n:
            return number
        counter +=1

print(get_nth_numbers(5))
    