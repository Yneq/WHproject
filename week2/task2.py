bookings={}
def available(consultant_name, hour, duration):
    if consultant_name in bookings:
        for start, end in bookings[consultant_name]:
            if not (hour >= end or (hour+duration) <= start):
                return False
    return True
    

def book(consultants, hour, duration, criteria):
    best_consultant = None
    best_value = float("inf") if criteria == "price" else 0
    for consultant in consultants:
        if available(consultant["name"], hour, duration):
            if consultant["price"] < best_value:
                best_consultant = consultant["name"]
                best_value = consultant["price"]
            elif consultant["rate"] > best_value:
                best_consultant = consultant["name"]
                best_value = consultant["rate"]
    if best_consultant:                    
        if best_consultant not in bookings:
            bookings[best_consultant] = []
        bookings[best_consultant].append((hour, hour + duration))
        return best_consultant
    else:
        return "No Service"

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

print(book(consultants, 15, 1, "price")) # Jenny 
print(book(consultants, 11, 2, "price")) # Jenny 
print(book(consultants, 10, 2, "price")) # John 
print(book(consultants, 20, 2, "rate"))# John 
print(book(consultants, 11, 1, "rate"))# Bob 
print(book(consultants, 11, 2, "rate"))# No Service 
print(book(consultants, 14, 3, "price")) # John