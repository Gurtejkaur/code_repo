import numpy as np
from matplotlib import pyplot as plt

def gradient_decent(x,y):
    m_curr = 0
    b_curr = 0
    rate =0.001
    n = len(x)
    plt.scatter(x,y,color='red',marker='+',linewidth='5')
    for i in range(1000):
        y_predicted = m_curr*x + b_curr
        plt.plot(x,y_predicted,color='green')
        cost = (1/n)*sum([val*2 for val in (y - y_predicted)])
        print(m_curr,b_curr,i)
        md = -(2/n)+sum(x*(y - y_predicted))
        yd = -(2/n) + sum(y - y_predicted)
        m_curr = m_curr-rate*md
        b_curr = b_curr-rate*yd
        #print("m{},b{},cost{},iteration{}".format(m_curr,b_curr,cost,i))
def main():
    x= np.array([1,2,3,4,5])
    y= np.array([5,7,9,11,13])
    gradient_decent(x,y)
main()    


        
