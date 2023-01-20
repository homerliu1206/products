#讀取檔案
products = []
with open ('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue  #跳至下一個迴圈<只能寫在迴圈中>
		name, price = line.strip().split(',')
		products.append([name,price])
print (products)

#讓使用者輸入
while True:
	name = input ('請輸入商品名稱:')
	if name == 'q' or name == 'Q':  #quit
		break
	price = input ('請輸入商品價格:')

	p = [] # 建立大清單中的小清單
	p.append(name)
	p.append(price)
	products.append(p)
print (products)

#印出所有購買紀錄
for p in products:
	print (p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: 
	f.write('商品'+ ',' + '價格' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')