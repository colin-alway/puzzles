#!/usr/bin/env python2.7
"""
GCHQ Christmas 2016 puzzle

Colin Alway 2016

Builds solution by alternately processing rows then columns until
all possible positions are exhausted.
"""
import itertools    # combinations
import math
import re
import sys

from data import *


ROW = 0
COL = 1


class Grid (object):
    """
    a container of cells
    make functions to set the access_mode to row or col
    then functions take (major,minor) or similar indices
    """
    def __init__(self):
        """
        """
        self.access_mode = ROW
        self.cells = [[None for ii in range(GRID_SIZE)] for jj in range(GRID_SIZE)]
        for (key,val) in cell_init.items():
            print key, val
            self.cells[key[0]][key[1]] = val
    
    def pprint(self):
        """
        uses get_cell_rc()
        need to add data arrays
        """
        pad = 4
        upper = [x/10 for x in range(GRID_SIZE)]
        lower = [x%10 for x in range(GRID_SIZE)]
        print ' ' * pad + ' '+' '.join(map(str,upper))
        print ' ' * pad + ' '+' '.join(map(str,lower))
        print ' ' * pad + pprint_header()
        for row in range(GRID_SIZE):
            print '  {0:2}'.format(row),
            for col in range(GRID_SIZE):
                cell = self.get_cell_rc(row, col)
                if cell is None:
                    print '.',
                elif cell == 0:
                    print ' ',
                else:   # cell == 1
                    print '#',
            print   # end line
        print ' ' * pad + pprint_header(delim='+', pad='-')
        
    def set_access_mode(self, mode):
        self.access_mode = mode

    def get_cell(self, line, item):
        if self.access_mode == ROW:
            return self.cells[line][item]
        if self.access_mode == COL:
            return self.cells[item][line]
        return 0
    
    def set_cell(self, line, item, val):
        if self.access_mode == ROW:
            self.cells[line][item] = val
        if self.access_mode == COL:
            self.cells[item][line] = val

    def get_cell_rc(self, row, col):
        return self.cells[row][col]

    def set_cell_rc(self, row, col, val):
        self.cells[row][col] = val

    def process(self, line_data_array, debug=False):
        for line_id in range(GRID_SIZE):
            combi_data = CombiData(line_data_array[line_id], GRID_SIZE)
            if debug:
                print '{0:28}'.format(line_data_array[line_id]), 
                print '{0:5}'.format(combi_data.max_combi)

            #iterate over combinations
            if combi_data.max_combi == 1:
                line = get_array_combi(line_data_array[line_id], GRID_SIZE, range(len(line_data_array[line_id])))
                if debug:
                    print line
                for col in range(GRID_SIZE):
                    self.set_cell(line_id, col, line[col])
                continue

            if combi_data.max_combi > 9:
                verbose = False
            else:
                verbose = True
                
            match_line = None
            # num_combi is number of valid combinations, could be max_combi if no cells are set on this line
            num_combi = 0
            for combi in itertools.combinations(range(combi_data.nn), combi_data.rr):
                line = get_array_combi(line_data_array[line_id], GRID_SIZE, combi)
                
                if debug and verbose:
                    print combi, ':', line
                
                # check if any known cells clash with pattern - if so skip this combination
                skip_line = False
                for index in range(GRID_SIZE):
                    cell = self.get_cell(line_id, index)
                    if cell is None:
                        continue
                    if cell != line[index]:
                        skip_line = True
                        break
                if skip_line:
                    continue
                    
                if match_line is None:
                    match_line = line
                else:   # do a per-item comparison of line & match_line - list comprehension!
                    match_line = [ii if ii==jj else None for ii,jj in zip(line, match_line)]
                num_combi += 1

            if debug and verbose:
                print combi, ':', match_line
            # step through match_line, setting cell values that are not None
            try:
                for index,val in enumerate(match_line):
                    if val is not None:
                        self.set_cell(line_id, index, val)
            except Exception, ee:   #TypeError
                print '>>>', ee
                print '>>> access_mode', self.access_mode
                print '>>> line_id', line_id
                print '>>> line_data_array', line_data_array[line_id]
                print '>>> line ', line
                
                print '>>> combi_data', combi_data
                print '>>> num_combi', num_combi
                print '>>> match_line', match_line
                raise ee


class CombiData (object):
    """
    use this to calc combinations from data arrays
    """
    def __init__(self, data_array, grid_size):
        # self.data_array = data_array #...?
        self.extra = grid_size - (sum(data_array) + len(data_array) - 1)
        self.rr = len(data_array)
        self.nn = len(data_array) + self.extra
        def nCr():
            """ maximum possible number of combinations """
            return math.factorial(self.nn) / (math.factorial(self.rr) * math.factorial(self.nn - self.rr))
        self.max_combi = nCr()
    
    def __str__(self):
        return '{0} {1} {2} {3} '.format(self.extra, self.rr, self.nn, self.max_combi)


def pprint_header(delim='|', pad='_'):
    """
    pretty print
    return: str to print
    """
    return delim+delim.join(pad * GRID_SIZE)+delim


def get_array_combi(data_array, grid_size, combi_array):
    """
    calc maximum combinations for an array of cells
    data_array : list of space-separated blocks
    grid_size : size of grid it must fit inside
    combi_array : array of items to select - from itertools.combinations()
    """
    result = [0] * grid_size    # initialise to 0's

    offset = 0
    for (index,size) in enumerate(data_array):
        
        head = offset + combi_array[index]
        result[head:head+size] = [1] * size
        
        offset += size

    return result


if __name__ == '__main__':

    print
    
    grid = Grid()
    grid.pprint()
    
    for loop in range(4):

        grid.set_access_mode(ROW)
        grid.process(row_data_array)
        grid.pprint()
        
        grid.set_access_mode(COL)
        grid.process(col_data_array)
        grid.pprint()
    
    sys.exit(0)

