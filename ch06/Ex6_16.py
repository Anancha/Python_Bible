shape_tuple1 = ("square","circle","triangle","rectangle","star")
shape_tuple2 = ("heart","oval")

print("shape_tuple1 = ",shape_tuple1)
print("shape_tuple2 = ",shape_tuple2)
length = len(shape_tuple1)
print("shape_tuple1 = ",length)

print("shape_tuple1[0] = ",shape_tuple1[0])
print("shape_tuple1[4] = ",shape_tuple1[4])
print("shape_tuple1[-5] = ",shape_tuple1[-5])
print("shape_tuple1[-1] = ",shape_tuple1[-1])
print("shape_tuple1[0:5] = ",shape_tuple1[0:5])
print("shape_tuple1[:5] = ",shape_tuple1[:5])
print("shape_tuple1[-4:] = ",shape_tuple1[-4:])

shape_tuple = shape_tuple1 + shape_tuple2
print("combine tuple1 and tuple2 = ",shape_tuple)