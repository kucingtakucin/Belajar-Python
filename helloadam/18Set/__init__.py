#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("===== SET ======")

# Set adalah semacam himpunan
superhero = set()
superhero.add("Captain America")
superhero.add("Ironman")
superhero.add("Thor")
superhero.add("Hulk")
superhero.add("Black Panther")
print(superhero)

ganjil = {1, 3, 5, 7, 9}
genap = {0, 2, 4, 6, 8}
prima = {1, 2, 3, 5, 7}
print(ganjil.union(genap))
print(ganjil.intersection(prima))

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
