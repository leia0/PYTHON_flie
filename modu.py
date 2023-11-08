#此檔案命名為modu.py
#modu.py當作module使用

class test1:
	def __init__(self):
		print("create") 
	
def fun1( ):
	print("function")
	return( ) 

#當作module使用時，__name__將不會是'__main__' 
if __name__ == '__main__':
	print("testmu!")