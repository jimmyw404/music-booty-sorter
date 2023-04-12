import os
import combiner

src_directory = "H:/m/Rhapsody of Fire/fav_food"
dst_directory = "H:/m/Rhapsody of Fire/fav"

comb = combiner.Combiner(src_directory, dst_directory)
comb.combine()