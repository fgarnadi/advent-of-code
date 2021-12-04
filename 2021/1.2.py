from sys import stdin

if __name__ == '__main__':
    up = 0
    window = []
    window_size = 3
    before = float('inf')
    for line in stdin:
        window.append(int(line))

        if len(window) == window_size:
            curr = sum(window)
            print(curr, before)
            if curr > before:
                up += 1

            before = curr
        
        if len(window) >= window_size:
            window.pop(0)
    
    print(up)