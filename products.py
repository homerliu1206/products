products = []
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


for p in products:
	print (p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:  #'w'表「寫入模式」
#若已有檔案，會以新檔案覆蓋
#若無檔案則會新增一個新檔案

	f.write('商品'+ ',' + '價格' + '\n')
	
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
		# 此行才是真正的寫入動作
		# 'abc' + '123' = 'abc123'
		# 'abc' * 3 = 'abcabcabc'


