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
