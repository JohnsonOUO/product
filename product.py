import os # operating system

def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if'商品,價格' in line:	
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products
			


#使用者輸入
def user_input(products):

	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入價格:')
		products.append([name,price])
		#p = [name]
		#p.append(name)
		#p.append(price)
		#products.append(p)	
	print(products)	
	print(products[0][1])
	return products

#印出購買紀錄	
def print_products(products):
	for p in products:
		print(p[0],'的價格是', p[1])
#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n'), 	
#檢查檔案
def main():		
	filename = 'products.csv'	
	if os.path.isfile(filename):
		print('有檔案')
		products = read_file(filename)	

	else:
			print('NO this item')	
			
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)			
main()	