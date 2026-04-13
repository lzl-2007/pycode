#试着通过iris数集复现一下简单的多分类神经网络
#这是一个算是比较成功的多分类神经网络
#导入一些奇怪的库，顺便记个时
#成功实现了在gpu上运行
import time
start=time.time()
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim 
from torch.utils.data import DataLoader,TensorDataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')#试着使用gpu
end=time.time()
print(f"成功导入这些库，用时{end-start:.3f}s")

def load_data():
    iris=load_iris()
    X,y=iris.data.astype(np.float32),iris.target   #直接导入的iris类似于一个字典，有许多索引
    print("数据集成功导入")
    return X,y,iris.target_names

X,y,names=load_data()
print(f"有这些分类种类:{names}")

def data_process(x,y,test_size=0.2,random_state=42):#这里将实现对数据划分为训练集和测试集，并且化为标准形式
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=test_size,random_state=random_state,stratify=y)
    scaler=StandardScaler()
    x_train=scaler.fit_transform(x_train).astype(np.float32)
    x_test=scaler.transform(x_test).astype(np.float32)      #测试集不需要fit计算参数（均值和标准差），直接沿用训练集的参数
    return x_train,x_test,y_train,y_test

x_train,x_test,y_train,y_test=data_process(X,y,test_size=0.3)

def dataload(x_train,y_train,batch_size=16,shuffle=False):#将训练集数据转化为可接受的dataset
    x_tensor=torch.tensor(x_train)
    y_tensor=torch.tensor(y_train,dtype=torch.long) #CrossEntropyLoss要求标签必须是long类型
    dataset=TensorDataset(x_tensor,y_tensor)  #dataload中的数据有类似索引的性质
    dataloader=DataLoader(dataset,batch_size=batch_size,shuffle=shuffle)#到了dataloader中就已经按照batch_size分出了批次
    return dataloader
train_dataloader=dataload(x_train,y_train,shuffle=True)
test_dataloader=dataload(x_test,y_test,shuffle=False)   #至此数据已经变成了可以塞进模型的格式，下面需要构建训练模型本身

class Mutiple(nn.Module):
    def __init__(self,input_size=4,hidden_size=16,class_nums=3):
        super(Mutiple,self).__init__()
        self.fc1=nn.Linear(input_size,hidden_size)
        self.relu=nn.ReLU()
        self.fc2=nn.Linear(hidden_size,hidden_size)
        self.fc3=nn.Linear(hidden_size,class_nums)#先只用两层试试
    
    def forward(self,x):
        out=self.fc1(x)
        out=self.relu(out)
        out=self.fc2(out)
        out=self.relu(out)
        out=self.fc3(out)
        return out
model=Mutiple()
print(model)

def train(model,dataloader,criterion,optimizer,num_epochs):    #开始训练模型
    loss_history=[]
    interval=max(1,num_epochs/10)
    n=0
    model.to(device)
    model.train()
    for epoch in range(num_epochs):
        n+=1
        num_epoch=0
        all_loss=0
        for data,label in dataloader:
            data=data.to(device)
            label=label.to(device)
            outputs=model(data)        #first calculate
            loss=criterion(outputs,label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            all_loss+=loss.item()
            num_epoch+=1
        
        avg_loss=all_loss/num_epoch
        loss_history.append(avg_loss)
        if n%interval==0:
            print(f"{n}/{num_epochs}has finished,loss:{avg_loss}")
    return loss_history

criterion=nn.CrossEntropyLoss()
#optimizer=optim.SGD(model.parameters(),lr=0.01)
optimizer=optim.Adam(model.parameters(),lr=0.001)#尝试一下Adam优化
loss_history=train(model,train_dataloader,criterion,optimizer,num_epochs=500)
def test_model(model,x_test,y_test):
    model.eval()
    with torch.no_grad():
        x_test_tensor=torch.tensor(x_test)
        x_test_tensor = x_test_tensor.to(device)
        outputs=model(x_test_tensor)
        _,predicted=torch.max(outputs,dim=1)   #这里取出的是最大值的索引实现分类，而不是值本身
        _, predicted = torch.max(outputs, dim=1)
        predicted = predicted.cpu().numpy()  # 先移到CPU再转numpy
    print(predicted)
    print(y_test)
    accuracy=(predicted==y_test).sum()/len(y_test)
    print(f"准确率为{(predicted==y_test).sum().item()}/{len(y_test)}")
    return accuracy

test_model(model,x_test,y_test)

       


