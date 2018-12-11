
GRID_SIZE = 25

row_data_array = [
    [7,3,1,1,7],
    [1,1,2,2,1,1],
    [1,3,1,3,1,1,3,1],
    [1,3,1,1,6,1,3,1],
    [1,3,1,5,2,1,3,1],
    [1,1,2,1,1],
    [7,1,1,1,1,1,7],
    [3,3],
    [1,2,3,1,1,3,1,1,2],
    [1,1,3,2,1,1],
    [4,1,4,2,1,2],
    [1,1,1,1,1,4,1,3],
    [2,1,1,1,2,5],
    [3,2,2,6,3,1],
    [1,9,1,1,2,1],
    [2,1,2,2,3,1],
    [3,1,1,1,1,5,1],
    [1,2,2,5],
    [7,1,2,1,1,1,3],
    [1,1,2,1,2,2,1],
    [1,3,1,4,5,1],
    [1,3,1,3,10,2],
    [1,3,1,1,6,6],
    [1,1,2,1,1,2],
    [7,2,1,2,5],
]

col_data_array = [
            [7,2,1,1,7],
          [1,1,2,2,1,1],
    [1,3,1,3,1,3,1,3,1],
      [1,3,1,1,5,1,3,1],
      [1,3,1,1,4,1,3,1],
          [1,1,1,2,1,1],
        [7,1,1,1,1,1,7],
                [1,1,3],
        [2,1,2,1,8,2,1],
      [2,2,1,2,1,1,1,2],
            [1,7,3,2,1],
      [1,2,3,1,1,1,1,1],
            [4,1,1,2,6],
        [3,3,1,1,1,3,1],
            [1,2,5,2,2],
    [2,2,1,1,1,1,1,2,1],
        [1,3,3,2,1,8,1],
                [6,2,1],
          [7,1,4,1,1,3],
            [1,1,1,1,4],
          [1,3,1,3,7,1],
    [1,3,1,1,1,2,1,1,4],
          [1,3,1,4,3,3],
        [1,1,2,2,2,6,1],
          [7,1,3,2,1,1],
]

# for known terms, enter head here. None means fills next available space
# fill this out as you fill in the graph
col_head_dict = {
     0 : [0,8,None,None,18],
     1 : [0,6,None,None,18,24],
     2 : [0,2,6,8,12,14,18,20,24],
     3 : [0,2,6,8,None,18,20,24],
     4 : [0,2,6,None,None,18,20,24],
     5 : [0,6,None,None,18,24],
    
     7 : [1,None,None],                 # get first block off first row
    
    16 : [0,2,6,10,13,15,24],
    17 : [1,None,None],                 # get first block off first row
    
    18 : [0,8,None,None,None,None],
    19 : [0,6,None,None,None],
    20 : [0,2,6,None,None,None],
    21 : [0,2,6,None,None,None,None,None,None],
    22 : [0,2,6,None,None,None],
    23 : [0,6,None,None,None,None,None],
}

'''
map known filled in cells here. in theory i guess this could be filled in by the
algorithm to produce the actual answer?
anyway, for now use it to check that the block positions do not clash with
known filled cells. store a tuple key (row,col) for every filled cell
'''
cell_map = {
    ( 3, 3) : 1,
    ( 3, 4) : 1,
    ( 3,12) : 1,
    ( 3,13) : 1,
    ( 3,21) : 1,
    # 8,
    # 16,
    # 21,
}


cell_init = {
    ( 3, 3) : 1,
    ( 3, 4) : 1,
    ( 3,12) : 1,
    ( 3,13) : 1,
    ( 3,21) : 1,
    ( 8, 6) : 1,
    ( 8, 7) : 1,
    ( 8,10) : 1,
    ( 8,14) : 1,
    ( 8,15) : 1,
    ( 8,18) : 1,
    (16, 6) : 1,
    (16,11) : 1,
    (16,16) : 1,
    (16,20) : 1,
    (21, 3) : 1,
    (21, 4) : 1,
    (21, 9) : 1,
    (21,10) : 1,
    (21,15) : 1,
    (21,20) : 1,
    (21,21) : 1,
}

