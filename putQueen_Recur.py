import time


def putQueen(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N):
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]:
            b[r] = c
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0
            if r == N-1:
                # print(b)
                numSol += 1
                #print("solutions:%d" % numSol)
            else:
                putQueen(r+1, b, colFree, upFree, downFree)
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1


for i in range(2, 12):
    ip = i
    start_time = time.time()
    N = ip

    numSol = 0  	# number of solutions

    b = N*[-1]  	# indices = rows, b[index] = coloumn, first init to -1
    colFree = N*[1] 			# all N col are free at first
    upFree = (2*N - 1)*[1] 		# all up diagonals are free at first
    downFree = (2*N - 1)*[1]    # all down diagonals are free at first

    putQueen(0, b, colFree, upFree, downFree)  # first add at 1st  (ie. row 0)
    print("N : %d" % ip)
    print("Process finished --- %.4f seconds ---" % (time.time() - start_time))
