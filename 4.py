import numpy as np

answer = 0

# Parse world with a padding of empty space to ensure that each scroll can look in a 3x3 vicinity.
# '.' = 0
# '@' = 1
has_scroll = np.pad(np.array([[u == '@' for u in e.strip()] for e in open(0)], dtype=int), 1)

# Remove until nothing to remove
while True:

    # 3x3 Kernel (Each element will contain scrolls in 3x3 vicinity)
    vert = np.roll(has_scroll, 1, 0) + has_scroll + np.roll(has_scroll, -1, 0) # Vertical kernel
    scroll_count = np.roll(vert, 1, 1) + vert + np.roll(vert, -1, 1)           # Horizontal kernel

    # Removal condition (Scroll count in a 3x3 vicinity is actually max 4 if you count resident scroll)
    remove = has_scroll & (scroll_count <= 4)

    remove_count = remove.sum()

    # > Part 1
    if answer == 0:
        print(remove_count)

    answer += remove_count

    # Break if there's nothing to remove
    if remove_count == 0:
        break

    # Remove free scrolls
    has_scroll &= ~remove

# > Part 2
print(answer)
