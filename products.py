# 重複輸入就需要用到迴圈，不知道要輸入幾次的情況下，適合用while loop
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name, price] # 下面3行是本行簡寫
	# p = [] # 建立一個子清單
	# p.append(name) # 把成對的資訊加入這個子清單
	# p.append(price) # 同上列
	products.append(p) # 靶子清單p加入大清單，則大清單的每項都由子清單組成，子清單內有成對的資訊
		# 也可以不建立p，直接寫products.append([name, price])
print(products) # 得出用[]包住的成對的[商品, 價格]

products[0][0] #表示product這個大清單的第一個項目也就是第一個p拿出來，又把p這個子清單的第一個項目拿出來，此處在本案例表示第一個商品的名稱

for p in products:
	print(p[0]) # 表示把每一個子清單p的第一個項目從product這個大清單中拿出來，所以會印出每個商品的名稱
