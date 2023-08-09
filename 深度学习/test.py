import scipy.signal
input1 = [[3,2,5,3,0], [3,4,1,0,3],[4,2,5,2,1],[4,1,4,6,2],[0,3,4,2,5]]
input2 = [[3,2,5],[3,4,1],[4,2,5]]
result = scipy.signal.convolve(input1, input2, mode ="valid")
print(result)