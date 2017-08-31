
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

#determine number of paths in a grid from left bottom (0,0) to reach (m,n) top right
#moves allowed are up and right.
#To move to (m,n) from (0,0) you need exactly 'm' right moves and 'n' up moves
#Fix 'm' right moves among the total 'm+n' moves
#(m+n) choose (m)
def combinatorial(total,k):
    return ((fact(total)) / ((fact(k) * fact(total -k))))
    #number of paths possible is returned



#number of paths in a grid when there is a hole / blockade in between
def find_paths(destination = (0,0), hole = (0,0)):
    total_moves_until_destination = destination[0]+destination[1] # not considering holes
    total_moves_until_hole = hole[0]+hole[1] # considering holes from (0,0) to hole
    total_moves_beyond_hole = (destination[0] - hole[0]) + (destination[1] - hole[1]) # considering holes from hole to destination

    possibl_moves_until_destination = combinatorial(total_moves_until_destination,destination[0])
    possibl_moves_until_hole = combinatorial(total_moves_until_hole,hole[0])
    possibl_moves_beyond_hole = combinatorial(total_moves_beyond_hole,destination[0]-hole[0])

    paths_thro_hole = possibl_moves_until_hole * possibl_moves_beyond_hole
    return (possibl_moves_until_destination - paths_thro_hole)


    
#number of paths when there are multiple holes
#better a dynamic iterative approach.
#first identify base cases where there is no dependancy and add value
#then solve dependancies in order
#base cases are (0,0) = origin,
#(i,0) = Bottom row. to reach a point (i,0) the only possible move is from (i-1,0). not possible to reach from downwards and we are already in bottom row
#(0,j) = Left column. to reach a point (0,j)the only possible move is from (0,j-1). not possible to reach from left and we are already in left column
nr_paths = {}

def paths(i,j):
    global nr_paths    

    if (i,j) in nr_paths:
        return nr_paths[i,j]
        
    elif i == 0 and j == 0:
        nr_paths[0,0] = 1
        return nr_paths[0,0]
        
    elif i == 0:
        nr_paths[0,j] = paths(0,j-1)
        return nr_paths[0,j]
        
    elif j == 0:
        nr_paths[i,0] = paths(i-1,0)
        return nr_paths[i,0]
        
    else:
        nr_paths[i,j] = paths(i-1,j)+ paths(i,j-1)
        return nr_paths[i,j]


#clearing nr_paths before executing this program so that info on holes are updated
        
def find_paths_dyn(destination = (0,0), holes = [()]):
    nr_paths.clear()
    for hole in holes:
        nr_paths[(hole)] = int(0)
    print (paths(destination[0],destination[1]))

    return


