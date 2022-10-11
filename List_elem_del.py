#Delete a elment in a list 
week=['saturday','sunday','monday','tuesday','wednesday']
print('week [0] : ',week[0])
print('week [-1] : ',week[-1])
print('week [-2] : ',week[-2])
print('week [-3] : ',week[-3])
print('week [-4] : ',week[-4])


print('before Deletion :',week)
del week[-1]
print()
print('After deletion : ',week)
del week[-3]
print()
print('After deletion : ',week)

#after deletion the indexing of element also change