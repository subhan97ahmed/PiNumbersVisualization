import matplotlib.pyplot as plt
import numpy as np
import math_pi

# Constants
REVERSED_DIGIT_OFFSET = 9
COLOR_CODE = 0

all_white_background = False
grid_size = 100
pi_digits_str = math_pi.pi(2, 1000000)
pi_digits_str = "1" + pi_digits_str
print(pi_digits_str)
pi_digits = [int(digit) for digit in pi_digits_str]
grid_reverse = np.zeros((grid_size, grid_size), dtype=np.uint8)


def apply_background_offset(digit, white_background):
    if white_background:
        return 100  # White background
    return REVERSED_DIGIT_OFFSET - digit


def create_heatmap(grid, color_digit_sequence=[]):
    sequence_length = len(color_digit_sequence)
    count = 0
    for i in range(grid_size):
        for r in range(grid_size):
            digit_index = (i * grid_size + r) % len(pi_digits)
            digit = pi_digits[digit_index]
            grid[i, r] = apply_background_offset(digit, all_white_background)
            if len(test_digits) > 0:
                if digit == color_digit_sequence[count]:
                    count += 1
                    if count == sequence_length:
                        for q in range(sequence_length):
                            grid[i, r - q] = COLOR_CODE
                        count = 0
                else:
                    count = 0


test_digits = []
create_heatmap(grid_reverse)

plt.imshow(grid_reverse, cmap='hot')
plt.axis("off")
plt.savefig('pi_heatmap.png', bbox_inches='tight', pad_inches=0, dpi=100)
plt.show()
