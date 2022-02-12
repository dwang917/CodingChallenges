#Commented out input manipulation for unit test

# first = input("")
# width, part_count = first.split()
# width = int(width)
# part_count = int(part_count)

# second = input("")
# partitions = second.split()


def solve_spaces(width, partitions):
    partitions = [int(item) for item in partitions]
    #add distance 0 and the max distance for calculation
    partitions.append(0)
    partitions.append(width)
    partitions.sort()

    # I chose a set for the calculation results, so we don't have to worry about repetition
    space_set = set()

    # calculate the distance between each combination of the partitions, and add them to the set
    for i in range(len(partitions)):
        for j in range(i+1, len(partitions)):
            space = partitions[j] - partitions[i]
            space_set.add(space)

    #commented out because unit tests don't use print
    # for item in sorted(space_set):
    #     print(item, end=" ")

    return(sorted(space_set))
