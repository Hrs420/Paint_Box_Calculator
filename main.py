import math
def paint_calc(height,width,cover):
  no_of_cans = math.ceil((height*width)/cover)
  print(no_of_cans)



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
