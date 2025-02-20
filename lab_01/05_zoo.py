zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
birds = ['rooster', 'ostrich', 'lark', ]
zoo.insert(1,'bear')
zoo.append(birds[0])
zoo.append(birds[1])
zoo.append(birds[2])
zoo.pop(3)
print(zoo)
print("лев в клетке", zoo.index('lion')+1, ",", "жаворонок в клетке",zoo.index('lark')+1)