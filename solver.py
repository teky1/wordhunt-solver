
get_rc = lambda i : (i >> 2, i & 3)
from_rc = lambda r, c : 4*r + c

print(f"Loading words file...")

with open("words.txt") as f:
    words = set(f.read().split())

print(f"Words file loaded. Processing words...")

almost = set()

for word in words:
    for i in range(1,len(word)):
        almost.add(word[0:i])



print(f"Finished processing words.")

def solve(board):
    all_words = []

    for i in range(len(board)):
        all_words += recurse(board, (i,))
    
    all_words.sort(key=lambda w : len(w), reverse=True)
    
    out = []
    seen_words = set()
    for w in all_words:
        # print("".join([board[x] for x in w]))
        word_str = "".join([board[x] for x in w])

        if len(word_str) <= 2 or word_str in seen_words:
            continue
        
        seen_words.add(word_str)

        out.append(([get_rc(x) for x in w], word_str))
    
    return out

def recurse(board, path):

    out = []

    curr_state = "".join([board[x] for x in path])
    if curr_state in words:
        out.append(path)
    if curr_state not in almost:
        return out
    
    neighb = get_valid_neighbors(path)
    for n in neighb:
        out += recurse(board, path+(n,))
    
    return out


def get_valid_neighbors(path):
    r, c = get_rc(path[-1])

    dirs = ((-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    out = []

    for dr, dc in dirs:
        if not (0 <= r+dr < 4 and 0 <= c+dc < 4):
            continue

        new_i = from_rc(r+dr, c+dc)
        if new_i not in path:
            out.append(new_i)
    
    return out

    

solve("TBAMVDIAHDRRACAY")