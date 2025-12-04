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

    is_p1 = answer == 0

    # Add removals to tally
    answer += remove.sum()

    # Print answer to p1
    if is_p1:
        print(answer)

    # Break if nothing to remove
    if not remove.sum():
        break

    # Remove free scrolls
    has_scroll = has_scroll & ~remove

# Print answer to p2
print(answer)
