# Comment these depending which to build
from rect_coord import *
#from tri_coord import *

def make_path(turn_arr):
    """Takes a strictly-increasing set turn_arr (ie. the input from
    the prime number generator or other generator) and tests the
    natural numbers on them. If the number tested is in turn_arr, then
    tell the "ant" to turn left. Otherwise, continue going straight.
    In either case, the path the "ant" takes is added to a hash table.
    If the path the ant takes is already in the hash table (ie. the
    "ant" takes a path that it has taken before), then add to the
    count of the entry in the hash table. Finally, the function
    returns a hash table of the path the ant took consisting of the
    form:
    
        hash_table: {(x,y,side): count, ...}

    """
    i,n = 0,1
    hash_table = {}
    ant_pos = (0,0,0)  # arbitrary starting side
    while i < len(turn_arr):
        next_turn = turn_arr[i]
        hash_table[ant_pos] = hash_table.get(ant_pos,0) + 1
        if n == next_turn:
            ant_pos = turn_left(ant_pos)
            i += 1
        else:
            ant_pos = go_straight(ant_pos)
        n += 1
    # add the last turn (ie. always ends on a turn)
    hash_table[ant_pos] = hash_table.get(ant_pos,0) + 1
    return hash_table
