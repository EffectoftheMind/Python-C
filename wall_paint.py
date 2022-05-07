import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height*wall_width
print('Wall area:', wall_area, 'square feet')
   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall

paint_cover = 350
needed_paint = wall_area/paint_cover
print('Paint needed:', "{:.2f}".format(needed_paint), 'gallons') #formats needed_paint to have 2 decimal points

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer

print("Cans needed:", math.ceil(needed_paint), "can(s)")

# FIXME (4): Calculate and output the total cost of paint can needed depending on color

print()
red_cost = 35
blue_cost = 25
green_cost =23

color_pick = input("Choose a color to paint the wall:")

if color_pick == 'red':
    total_cost = red_cost * math.ceil(needed_paint)
    print("\nCost of purchasing red paint:", "$"+str(total_cost))
if color_pick == 'blue':
    total_cost = blue_cost * math.ceil(needed_paint)
    print("\nCost of purchasing blue paint:", "$"+str(total_cost))
if color_pick == 'green':
    total_cost = green_cost * math.ceil(needed_paint)
    print("\nCost of purchasing green paint:", "$"+str(total_cost))
