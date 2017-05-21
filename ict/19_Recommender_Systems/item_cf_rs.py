#-*-coding:utf-8-*-  

import math  
  
class ItemBasedCF:  
	def __init__(self,train_file):  
		self.train_file = train_file  
		self.readData()  
	def readData(self):  
		#��ȡ�ļ����������û�-��Ʒ�����ֱ�Ͳ��Լ�  
		self.train = dict()     #�û�-��Ʒ�����ֱ�  
		for line in open(self.train_file):  
			# user,item,score = line.strip().split(",")  
			user,score,item = line.strip().split(",")  
			self.train.setdefault(user,{})  
			self.train[user][item] = int(float(score))  

	def ItemSimilarity(self):  
		#������Ʒ-��Ʒ�Ĺ��־���  
		C = dict()  #��Ʒ-��Ʒ�Ĺ��־���  
		N = dict()  #��Ʒ�����ٸ���ͬ�û�����  
		for user,items in self.train.items():  
			for i in items.keys():  
				N.setdefault(i,0)  
				N[i] += 1  
				C.setdefault(i,{})  
				for j in items.keys():  
					if i == j : continue  
					C[i].setdefault(j,0)  
					C[i][j] += 1  
		#�������ƶȾ���  
		self.W = dict()  
		for i,related_items in C.items():  
			self.W.setdefault(i,{})  
			for j,cij in related_items.items():  
				self.W[i][j] = cij / (math.sqrt(N[i] * N[j]))  
		return self.W  

	#���û�user�Ƽ���ǰK������û�  
	def Recommend(self,user,K=3,N=10):  
		rank = dict()  
		action_item = self.train[user]     #�û�user��������Ϊ��item������  
		for item,score in action_item.items():  
			for j,wj in sorted(self.W[item].items(),key=lambda x:x[1],reverse=True)[0:K]:  
				if j in action_item.keys():  
					continue  
				rank.setdefault(j,0)  
				rank[j] += score * wj  
		return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N])  
	  
#����һ��ItemBased�Ƽ��Ķ���      
Item = ItemBasedCF("uid_score_bid")  
Item.ItemSimilarity()  
#print Item.ItemSimilarity()
recommedDic = Item.Recommend("xiyuweilan")  
for k,v in recommedDic.iteritems():  
	print k,"\t",v  
	
	