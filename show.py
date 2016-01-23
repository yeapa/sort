import matplotlib.pyplot as plt
import numpy as np

def showList(data_lists):
    data_num=len(data_lists)
    plt.figure()
    for i,data_list in enumerate(data_lists):
        data_length=len(data_list)
        p=plt.subplot(data_num,1,i+1)
        p.bar(np.arange(data_length), data_list, color='r', width=0.2)
        plt.xticks(np.arange(data_length) + 0.1, data_list)  # Translation
        # plt.yticks(num_list)
        plt.grid(True)
        plt.hold()
        plt.title("sort")
    plt.show()

if __name__=="__main__":
    a=[1,3,5]
    b=[2,4,3,6]
    data_lists=[]
    data_lists.append(a)
    data_lists.append(b)
    showList(data_lists)