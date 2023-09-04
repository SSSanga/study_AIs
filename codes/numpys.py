# 2차원 list
py_list = [[1,2]
           ,[3,4]
           ,[5,6]]


import numpy as np
# 행렬(=array)
np_array = np.array([[7,8]
                    ,[9,10]
                    ,[11,12]])

# 타입 확인
# type(py_list)
# <class 'list'>
# type(np_array)
# <class 'numpy.ndarray'>

# 행렬의 장점
# - loop보다 계산 속도가 빨라짐

# 평균(mean)
# 1. np.mean(np_array) : 7~12 까지의 전체 평균 계산
#    9.5
# 2. np.mean(np_array, axis=0) : 열 단위로 평균 계산
#    array([ 9., 10.])
# 3. np.mean(np_array, axis=1) : 행 단위로 평균 계산
#    array([ 7.5,  9.5, 11.5])



# 병합(concat)
np_array02 = np.array(py_list)
# np.concatenate((np_array, np_array02), axis=0) : 열을 기준으로 병합(아래로 붙음)
# array([[ 7,  8],
#       [ 9, 10],
#       [11, 12],
#       [ 1,  2],
#       [ 3,  4],
#       [ 5,  6]])
# np.concatenate((np_array, np_array02), axis=1) : 행을 기준으로 병합(옆으로 붙음)
# array([[ 7,  8,  1,  2],
#       [ 9, 10,  3,  4],
#       [11, 12,  5,  6]])
# 병합 시 두 개의 데이터프레임의 size가 동일해야 한다

pass

