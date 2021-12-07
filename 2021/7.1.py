def calculate_fuel(crabs, pos):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - pos)

    return fuel


if __name__ == "__main__":
    crabs = list(map(int, str(input()).split(",")))
    _max = max(crabs)

    fuel = float("inf")
    for i in range(_max):
        fuel = min(fuel, calculate_fuel(crabs, i))

    print(fuel)
