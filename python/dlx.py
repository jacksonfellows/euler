class Node:
    def __init__(self):
        self.l = self.r = self.u = self.d = self.c = None

class ColNode(Node):
    def __init__(self):
        super().__init__()
        self.s = 0

class RowNode(Node):
    def __init__(self, i):
        super().__init__()
        self.i = i

def matrix_to_nodes(mat):
    cols = [ColNode() for _ in mat[0]]

    root = Node()
    root.l = cols[-1] if len(cols) > 0 else root
    root.r = cols[0] if len(cols) > 0 else root

    # stitch columns together
    for i,col in enumerate(cols):
        col.l = cols[i-1] if i > 0 else root
        col.r = cols[i+1] if i < len(cols) - 1 else root

    # add nodes
    bottom_row = cols.copy()
    for nrow,row in enumerate(mat):
        current_row = []
        for i,x in enumerate(row):
            if x:
                node = RowNode(nrow)
                node.c = cols[i]
                node.c.s += 1
                node.u = bottom_row[i]
                bottom_row[i].d = node
                bottom_row[i] = node
                current_row.append(node)
        # link row
        for i,node in enumerate(current_row):
            node.l = current_row[i-1]
            node.r = current_row[(i+1) % len(current_row)]

    # loop back
    for i,node in enumerate(bottom_row):
        cols[i].u = node
        node.d = cols[i]

    return root

def search(h, o=[]):
    if h.r == h:
        yield [r.i for r in o]
    else:
        c = choose_col(h)
        cover(c)

        r = c.d
        while r != c:
            o.append(r)

            j = r.r
            while j != r:
                cover(j.c)
                j = j.r

            yield from search(h, o)

            r = o.pop()
            c = r.c

            j = r.l
            while j != r:
                uncover(j.c)
                j = j.l

            r = r.d
        uncover(c)

def cover(c):
    c.r.l, c.l.r = c.l, c.r
    i = c.d
    while i != c:
        j = i.r
        while j != i:
            j.d.u, j.u.d = j.u, j.d
            j.c.s -= 1
            j = j.r
        i = i.d

def uncover(c):
    i = c.u
    while i != c:
        j = i.l
        while j != i:
            j.c.s += 1
            j.d.u = j.u.d = j
            j = j.l
        i = i.u
    c.r.l = c.l.r = c

def choose_col(h):
    c = None
    s = float('inf')
    j = h.r
    while j != h:
        if j.s < s:
            c = j
            s = j.s
        j = j.r
    return c

def dlx_search(matrix):
    return search(matrix_to_nodes(matrix))
