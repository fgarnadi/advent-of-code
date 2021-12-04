from sys import stdin

if __name__ == '__main__':
    up = 0
    before = float('inf')
    for line in stdin:
        x = int(line)

        if x > before:
            up += 1
        
        before = x
    print(up)