import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


# 초기하분포
[M, n, N] = [,,]
stat_hyp = 

# 그리기
fig, ax = plt.subplots()
## pmf를 만드는 코드를 작성해 주세요
x_axis = np.arange(n + 1) 
plt.bar()


##
plt.show()
fig.savefig("pmf_plot.png")


# Q2. 초기하분포 cdf 그리기 
## cdf 만드는 코드를 작성해 주세요
x_axis = np.arange(n + 1) 
plt.bar()


##
plt.show()
fig.savefig("cdf_plot.png")


# Q3. 랜덤표본 추출
## seed 설정 seed = 0 


## 랜덤 샘플 추출
random_hyp = 
print(random_hyp)
## 평균계산
hyp_mean = 
print(hyp_mean)
