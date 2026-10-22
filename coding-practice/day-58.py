def warehouse_delivery(warehouse, commands):
    failed_moves = 0
    packages_carried = 0
    packages_delivered = 0
    collected = set()

    # Find the starting position
    for i in range(len(warehouse)):
        if "S" in warehouse[i]:
            starting_point = [i, warehouse[i].index("S")]
            break

    # Process each command
    for command in commands:
        new_row = starting_point[0]
        new_col = starting_point[1]

        if command == "U":
            new_row -= 1
        elif command == "D":
            new_row += 1
        elif command == "R":
            new_col += 1
        elif command == "L":
            new_col -= 1

        # Check whether the move is outside the grid
        if (new_row < 0 or new_row >= len(warehouse)
                or new_col < 0 or new_col >= len(warehouse[0])):
            failed_moves += 1
            continue

        # Check whether the move hits an obstacle
        if warehouse[new_row][new_col] == "#":
            failed_moves += 1
            continue

        # Update the robot's position
        starting_point = [new_row, new_col]

        # Collect each package only once
        if warehouse[new_row][new_col] == "P":
            if (new_row, new_col) not in collected:
                packages_carried += 1
                collected.add((new_row, new_col))

        # Deliver all carried packages
        if warehouse[new_row][new_col] == "D":
            packages_delivered += packages_carried
            packages_carried = 0

    # Return the final result after all commands
    final_row = starting_point[0]
    final_col = starting_point[1]

    return (
        final_row,
        final_col,
        failed_moves,
        packages_delivered,
        packages_carried
    )


warehouse = [
    "S..P.",
    ".#...",
    "P...D",
    "..#.."
]

print(warehouse_delivery(warehouse, "RRDLL"))
