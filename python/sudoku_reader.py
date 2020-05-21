def read_boards(f):
    boards = []
    for i,line in enumerate(f):
        if i % 10 == 0:
            boards.append([])
        else:
            boards[-1].append([int(d) for d in line.strip()])
    return boards
