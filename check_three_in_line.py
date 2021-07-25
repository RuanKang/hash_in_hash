def check_three_in_line(board):
    same_line = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for n1, n2, n3 in same_line:
        if board[n1] != 0 and board[n1] == board[n2] and board[n2] == board[n3]:
            return True
    return False

test_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],

    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0],

    [1, 1, 1, 0, 0, 0, -1, -1, -1],
    [1, 1, 1, 0, 0, 0, -1, -1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, -1, 1, 1, 0, 0, 1],

    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 1, 1, -1, 0, -1, 0],

    [1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, -1, -1, 1, 1, 1, -1, -1],
    [1, 1, -1, -1, 1, 1, -1, -1, 0],
    [1, 1, -1, -1, 1, 1, -1, -1, 1],
]

expected_output = [
    False,
    False,
    False,
    False,

    False,
    False,
    False,

    True,
    True,
    True,
    True,

    False,
    False,

    True,
    False,
    False,
    True
]

def test():
    for input_data, expected in zip(test_data, expected_output):
        got = check_three_in_line(input_data) 
        if got is not expected:
            print("[FAILED] input: {}, expected: {}, got: {}".format(input_data, expected, got))
        else:
            print("[  OK  ] input: {}, expected: {}, got: {}".format(input_data, expected, got))

if __name__ == "__main__":
    test()
