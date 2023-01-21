import os  # operating system

#讀取檔案
def read_file (filename):
	products = []
	with open (filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue  #跳至下一個迴圈<只能寫在迴圈中>
			name, price = line.strip().split(',')
			products.append([name,price])
	return products

#讓使用者輸入
def user_input (products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print (p[0], '的價格是', p[1])

#寫入檔案
def write_file (filename, products):
	with open (filename, 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

#main function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  #檢查檔案是否存在
		print ('包含檔案')
		products = read_file  (filename)
	else:
		print ('找不到檔案！')

	products = user_input (products)
	print_products (products)
	write_file ('products.csv', products) 

main()