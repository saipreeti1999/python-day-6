x=[12,24,35,24,88,120,155,88,120,155]
dup_items=set()
uniq_items=[]
for i in x:
    if i not in dup_items:
        uniq_items.append(i)
        dup_items.add(i)
print(uniq_items)
