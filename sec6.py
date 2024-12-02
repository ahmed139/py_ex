#ex. 24_6 extract extension from filename
filename = "view.jpg"
ext = filename.split('.')[1]
print(ext)

#ex. 25_6 
st = '323-fdf-fdfd'
print(st[:3]+st[-3:])

#ex.26_6
bin = '1 0 0 1 0 1'
#removing spaces tech 1 using list comprehension
st_bin = [int(x) for x in bin if x !=' ']
print(st_bin)
w = [2**x for x in range(len(st_bin))]
w =w[::-1]
print(w)
w_bin= [x*2**(len(st_bin)-index-1) for index,x in enumerate(st_bin)] 
#dec = sum([x*i for x in st_bin, for i in range(len(st_bin))])
print(w_bin)
print(f"Final Decimal = {sum(w_bin)}")

#ex. 30_7 

# check if a value from instance


flag = True
print(isinstance(flag,bool))


#ex.31_7

