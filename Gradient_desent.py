import numpy as np
def gradient_desent(x,y):
    m_curr= b_curr= 0
    iterations= 10000 #let
    n= len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted= m_curr * x + b_curr
        cost= 1/n * sum([val **2 for val in (y- y_predicted)]) #mean square error (cost function)
        md = -(2/n) * sum(x*(y-y_predicted)) #derivative of m_curr
        bd=  -(2/n) * sum(y-y_predicted)  #derivative of b_curr
        m_curr= m_curr - learning_rate* md
        b_curr= b_curr - learning_rate* bd
        print("m {}, b {}, cost {}, iterations {}".format(m_curr,b_curr,cost,i))


x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

# we have linear equation as y= 2x + 3 we are approaching m as 2 and b as 3
# m=(7-5)/(2-1)=2 and b =5 - (2*1)


gradient_desent(x,y)