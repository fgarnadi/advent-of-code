# represent fish life timer
pool_size = 9

days = 256

if __name__ == "__main__":
    initial = map(int, str(input()).split(","))
    fishes = [0] * pool_size
    for fish in initial:
        fishes[fish] += 1

    for _ in range(days):
        prev = 0
        for i in range(pool_size - 1, -1, -1):
            if i == 0:
                fishes[6] = fishes[6] + fishes[0]
                fishes[8] = fishes[0]
                fishes[0] = prev
            else:
                prev, fishes[i] = fishes[i], prev

    print(sum(fishes))
