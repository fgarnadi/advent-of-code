from sys import stdin

if __name__ == "__main__":
    bracket = {"]": "[", "}": "{", ")": "(", ">": "<"}
    bracket_rev = {"[": "]", "{": "}", "(": ")", "<": ">"}

    score_map = {")": 1, "]": 2, "}": 3, ">": 4}

    scores = []
    for line in stdin:
        chunk = []
        for nav in line.strip():
            if nav in bracket.values():
                chunk.append(nav)
            elif bracket.get(nav) != chunk.pop():
                chunk = []
                break

        score = 0
        if len(chunk) > 0:
            for val in chunk[::-1]:
                comp = bracket_rev.get(val)
                score = (score * 5) + score_map.get(comp)
            scores.append(score)

    print(sorted(scores)[len(scores) // 2])
