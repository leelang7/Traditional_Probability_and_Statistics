from elice_utils import EliceUtils
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
elice_utils = EliceUtils()    

# Q1. 이항분포pmf 그리기 
# 이항분포 생성
n, p = 
stat_bin = 

# 그리기
fig, ax = plt.subplots()
## pmf를 만드는 코드를 작성해 주세요
x_axis = np.arange(n + 1) 
plt.bar()


##
plt.show()
fig.savefig("pmf_plot.png")
elice_utils.send_image("pmf_plot.png")

# Q2. 이항분포cdf 그리기 
## cdf 만드는 코드를 작성해 주세요
x_axis = np.arange(n + 1) 
plt.bar()


##
plt.show()
fig.savefig("cdf_plot.png")
elice_utils.send_image("cdf_plot.png")


# Q3. 랜덤표본 추출
## seed 설정 seed = 0 


## 랜덤 샘플 추출
random_bin = 
print(random_bin)
## 평균계산
bin_mean = 
print(bin_mean)
