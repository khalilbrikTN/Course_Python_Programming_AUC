
def CirclesOfFriends(n, lst):
    circles = []

    for pair in lst:
        friend1, friend2 = pair
        found = False

        # check if either friend is already in an existing circle.
        for circle in circles:
            if (friend1 in circle) or (friend2 in circle):
                circle.update([friend1, friend2])
                found = True
                break

        # if neither friend is in an existing circle, create a new circle
        if not found:
            circles.append(set(pair))

    # create a set of all people to identify those not in any circles
    all_people = set(range(1, n + 1))
    for circle in circles:
        all_people -= circle

    # add remaining people as individual circles
    circles.append(all_people)

    # print the friend circles
    for i, circle in enumerate(circles):
        print(f"Friend Circle {i + 1} is {sorted(circle)}")



CirclesOfFriends(7, [(1, 2), (2, 3), (4, 6)])



