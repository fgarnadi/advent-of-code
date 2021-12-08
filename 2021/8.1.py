from sys import stdin

if __name__ == "__main__":

    counter = 0
    for line in stdin:
        signal, output = map(lambda s: s.strip().split(), line.split("|"))
        
        for out in output:
            match len(out):
                case 2 | 3 | 4 | 7:
                    counter += 1
                
    print(counter)
