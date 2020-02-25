from draw_engine import draw_map, create_graphic_map, update_map
from validator import Validator




if __name__ == "__main__":


   z = int(input('type size: '))



   map_graphic = create_graphic_map(z, z)
   map_validator = [[' ' for i in range(z)] for j in range(v)]
   validator = Validator(map_validator)



   for i in range(z * v):

      x = int(input('type coordinate one: '))
      y = int(input('type coordinate two: '))
      m = 0
      n = 0
      if i % 2:
         update_map(map_graphic, y, x, "cross")
         map_validator[x][y] = 'x'
         m += 1
      else:
         update_map(map_graphic, y, x, "circle")
         map_validator[x][y] = 'o'
         n += 1
      for line in map_validator:
         print(line)
      draw_map(map_graphic)
      if validator.validate():
         if m > n:
            print('cross wins')
         else:
            print('circle wins')
         break
      else:
         print("noone wins")




