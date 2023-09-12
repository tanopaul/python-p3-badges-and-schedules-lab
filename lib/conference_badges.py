def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    list_of_badge_names = [f"Hello, my name is {name}." for name in names]
    return list_of_badge_names

def assign_rooms(names):
    list_of_rooms = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return list_of_rooms

def printer(names):
    for i in range(len(names)):
        print(badge_maker(names[i]))
    print_rooms = assign_rooms(names)
    for j in range(len(print_rooms)):
        print(print_rooms[j])


printer(['Tano', 'Rice', 'Andrada'])