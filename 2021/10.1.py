from sys import stdin

if __name__ == "__main__":
    bracket = {"]": "[", "}": "{", ")": "(", ">": "<"}

    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

    score = 0
    for line in stdin:
        chunk = []
        for nav in line.strip():
            if nav in bracket.values():
                chunk.append(nav)
            elif bracket.get(nav) != chunk.pop():
                score += score_map.get(nav)
                break

    print(score)
