import random
def rand_array():
  length = random.randint(1,20)
  _2d_list = [[random.choice([1,0]) for y in range(length)] for x in range(random.randint(1,20))]
  _2d_list[random.randint(0,len(_2d_list)-1)][random.randint(0,len(_2d_list[0])-1)] = 0
  return _2d_list