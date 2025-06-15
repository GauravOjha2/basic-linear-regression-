import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_train=np.array([1,2,3,4])
y_train=np.array([6,7,8,9])

w=100
b=200

def compute_model_output(x,w,b):
    m=x.shape[0]
    f_wb=np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b

        return f_wb

tmp_f_wb = compute_model_output(x_train, w, b,)
plt.plot(x_train,tmp_f_wb, c='b',label='Our Prediction') # type: ignore
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')
plt.title("Housing Prices")
plt.ylabel('Price (in 1000s of dollars)')
plt.xlabel('Size (1000 sqft)')
plt.legend
plt.show


w = 200                         
b = 100    
x_i = 1.5
cost_1200sqft = w * x_i + b    

print(f"${cost_1200sqft:.0f} thousand dollars")