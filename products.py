# 做完下面那堆步驟創好檔案後，來讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f: # 讀取這個檔案的每一行
		if '商品,價格' in line: # 表示若遇到的是表頭'商品,價格'，就跳過，再跑下一回
			continue # 來教continue這個功能，相對於break會直接離開迴圈，continue會跳過這一回，又開始下一回從迴圈第一行開始
		name, price = line.strip().split(',') # split是切割行的意思，括號內表示碰到括號內東西的時候要換行，先放strip是為了先清掉換行符號
			# 因為有分割，所以可以直接分別命名分割好的東西
		products.append([name, price])
print(products)


# 重複輸入就需要用到迴圈，不知道要輸入幾次的情況下，適合用while loop
# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price) # price本來是字串，型別轉換為整數
	p = [name, price] # 下面3行是本行簡寫
	# p = [] # 建立一個子清單
	# p.append(name) # 把成對的資訊加入這個子清單
	# p.append(price) # 同上列
	products.append(p) # 靶子清單p加入大清單，則大清單的每項都由子清單組成，子清單內有成對的資訊
		# 也可以不建立p，直接寫products.append([name, price])
print(products) # 得出用[]包住的成對的[商品, 價格]

products[0][0] #表示product這個大清單的第一個項目也就是第一個p拿出來，又把p這個子清單的第一個項目拿出來，此處在本案例表示第一個商品的名稱

# 印出所有購買紀錄
for p in products:
	print(p[0]) # 表示把每一個子清單p的第一個項目從product這個大清單中拿出來，所以會印出每個商品的名稱

# 字串可用的符號
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'


#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:  # encoding是編碼的意思 (太複雜不說)
															# 此處表示要用要使用'utf-8'這個編碼，這是最廣泛使用的編碼
															# 這個編碼可以讀取大部分的符號
# 寫入products.csv這個檔案，w是編輯 (相對於r是讀取)，如果這個檔案原本不存在就會被創造出來，然後被稱為f
# 若原本存在，就會被覆寫
	f.write('商品,價格\n') # 在for loop開始前加入表頭
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 此處f.write才真的寫入f，也就是products.csv這個檔案
											# 然後清單中的資料就被存入這個檔案
											# 以csv存檔可以用excel開啟，','表示excel的分隔，'\n'表示換行
# 原本價格p[1]是字串，用int轉換為整束後，就不能用+跟p[0]這樣的字串加在一起了
# 所以在這裡要並在一起的時候，用str再度轉換為字串，就能用+合併了

# 出現亂碼，可以把csv或txt拖曳到subline裡面看他的顯示，如果沒有亂碼就表示編碼沒有問題，
	# 若csv或txt還是顯示亂碼，表示讀取有問題，就用資料來源從txt/csv選擇檔案原點為'utf-8'
