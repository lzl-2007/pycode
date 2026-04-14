import numpy as np
import matplotlib.pyplot as plt



data=np.array([676,825,774,716,940,1159,1384,1524,1668,1688,1958,2031,2234,2566,2820,3006,3093,3277,3514,3770,4107])#原始数据
def calculateloss(y_real,y_pred):
    n=len(y_real)
    loss=np.sqrt(sum([(y_pred[i]-y_real[i])**2 for i in range(n)])/n)
    return loss
a=0.3

def e_x(a,data):               #先尝试二次指数平滑，看起来预测明显滞后，误差较大
    n=len(data)
    predicted=[data[0]]
    for i in range(1,n):           #指数平滑如果以观测首值作为预测首值可以直接从第二个开始，不然每迭代一次首值就多出现一遍
        temp=a*data[i]+(1-a)*predicted[-1]
        predicted.append(temp)
    return predicted
e1_predicted=e_x(0.3,data)
e2_predicted=e_x(0.3,e1_predicted)
loss1=calculateloss(data,e2_predicted)
e2_predicted.append(e2_predicted[-1]*(1-a)+data[-1]*a)
t=np.array([i for i in range(1965,1987)])
data1=np.concatenate([data,[0]])#注意拼接两层括号
fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=[18,6])
ax1.scatter(t,data1,color='r',label="real values")
ax1.plot(t,e2_predicted,color="b",label=f"predicted by e2,\nloss={loss1}\n1986predict:{e2_predicted[-1]:.3f}")
ax1.legend()

#尝试线性拟合
t_real=np.array([i for i in range(1965,1986)])
result=np.polyfit(t_real,data,deg=1)
def func1(x):
    return result[0]*x+result[1]
t=np.array([i for i in range(1965,1987)])
y_pred2=func1(t)
loss2=calculateloss(func1(t_real),data)
ax2.scatter(t,data1,color='r',label="real values")
ax2.plot(t,y_pred2,color="b",label=f"predicted by linear polyfit,\nloss={loss2}\n1986predict:{y_pred2[-1]:.3f}")
ax2.legend()
#比较简单的线性拟合，似乎比二次指数平滑预测准确一点

#下面试图训练一个模型
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset,DataLoader
from sklearn.preprocessing import StandardScaler
print("导入库成功")
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x_train=np.array([[i] for i in range(1965,1986)])
y_train=np.array([[data[i]] for i in range(len(x_train))])
scalarx=StandardScaler()
scalary=StandardScaler()
x_scalar_train=torch.tensor(scalarx.fit_transform(x_train),dtype=torch.float32)
y_scalar_train=torch.tensor(scalary.fit_transform(y_train),dtype=torch.float32)
dataset=TensorDataset(x_scalar_train,y_scalar_train)#只接受张量，而且第一维形状要一样
dataload=DataLoader(dataset,batch_size=1,shuffle=True)

class Predicted(nn.Module):
    def __init__(self, input_size=1,hidden_size=16,output_size=1):
        super(Predicted,self).__init__()
        self.fc1=nn.Linear(input_size,hidden_size)
        self.relu=nn.ReLU()
        self.fc2=nn.Linear(hidden_size,hidden_size)
        self.fc3=nn.Linear(hidden_size,output_size)
    
    def forward(self,x):
        out=self.fc1(x)
        out=self.relu(out)
        out=self.fc2(out)
        out=self.relu(out)
        out=self.fc3(out)
        return out
    
model=Predicted()
model.train()
epoch_num=500
criterion=nn.MSELoss()
lr=0.005
optimizer=optim.SGD(model.parameters(),lr=lr)
loss_history=[]
interval=max(1,epoch_num/10)
thisloss=0
model.to(device)

for num in range(epoch_num):
    for input,label in dataload:
        input=input.to(device)#赋值之后转移设备才成功
        label=label.to(device)
        output=model(input)
        optimizer.zero_grad()
        loss=criterion(output,label)
        loss.backward()
        optimizer.step()
        thisloss+=loss
    avgloss=thisloss/num
    if (num+1)%interval==0:
        print(f"{num+1}/{epoch_num} finished,loss={avgloss}")

x_calloss=x_scalar_train.to(device)
y_calloss=model(x_calloss)
y_calloss=y_calloss.to('cpu').detach().numpy().reshape([1,-1])
x_calloss=x_calloss.to('cpu').detach().numpy().reshape([1,-1])
x_=scalarx.inverse_transform(x_calloss).reshape(-1)  #scaler只能接受二维结构
y_=scalary.inverse_transform(y_calloss).reshape(-1)
loss3=calculateloss(y_,data)

x_test=scalarx.transform(np.array([[i] for i in range(1960,1995)]))#刻意升维，否则后期一维容易不被接受
x_test=torch.tensor(x_test,dtype=torch.float32).to(device)
y_pred3=model(x_test)
x_draw=np.array([i for i in range(1965,1987)])
x_draw2=np.array([i for i in range(1960,1995)])
y_pred3=y_pred3.to('cpu').detach().numpy().reshape([1,-1])#张量转移到cpu且detach解梯度才能转numpy，转为二维投给scaler
y_draw=scalary.inverse_transform(y_pred3).reshape(-1)#解标准化，最后转为一维绘图
ax3.scatter(x_draw,data1,color='r',label="real values")
ax3.plot(x_draw2,y_draw,color="b",label=f"predicted by pytorch,\nloss={loss3}\n1986predict:{y_draw[-10]:.3f}")
ax3.legend()
plt.show()





