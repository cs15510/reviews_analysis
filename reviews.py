data = []
count=0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count+=1
		if count % 10000 == 0:
			print(len(data))
data_len = []
for i in range(len(data)):
	data_len.append(len(data[i]))
print("檔案讀取完了, 總共有",len(data),"筆資料")
print("平均留言長度為", (sum(data_len)/len(data)))