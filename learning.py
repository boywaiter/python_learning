def get_error_details():
	return (2,'details')
errnum,errstr=get_error_details()
print(errnum,errstr)
a,b=5,8
print(a,b)
a,b=b,a
print(a,b)

class OutOfRangeException(Exception):
	def __init__(self,item):
		Exception.__init__(self)
		self.item = item
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("Object initializing:")
	def __del__(self):
		print("Object destroyed.")
	def __str__(self):
		return "A object about {}".format(self.name)
	def __lt__(self,other):
		return self.age<other.age
	def __len__(self):
		return len(self.name)

	def __getitem__(self, item):
		try:
			if item>=len(self.name):
				raise(OutOfRangeException(item))
		except OutOfRangeException as ex:
				print("{} is out of range".format(ex.item))
		else:
			return self.name[item]

tom=Person('tom',24)
jerry=Person('jerry',30)
if tom<jerry:
	print(tom)
else:
	print(jerry)
print(tom[5])
print(tom[-2])


unsortedDict=[{'x':1,'y':3}, {'x':3,'y':1}]
unsortedDict.sort(key=lambda i:i['y'])
#return unsortedDict[i]['y']
print(unsortedDict)
#for i in range(0,len(unsortedDict)):
#	print(unsortedDict[i]['y'])

listone=[2,3,4]
listtwo=[2*i for i in listone]
print(listtwo)

def powersum(power,*args,**kwargs):
	total,count=0,0
	dict={}
	for num in args:
		total+=pow(num,power)
	for key in kwargs:
		count+=kwargs[key]
	return total, count
print(powersum(2,3,4,apple=100,pear=200))
print(powersum(2,5))

