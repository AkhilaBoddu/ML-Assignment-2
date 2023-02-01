def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
sample_list=[1,2,3,3,3,3,4,5]
print("Sample List :", sample_list)
print("Unique List :",unique_list(sample_list))



