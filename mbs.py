import os
import combiner

src_directory = "H:/m/Sabaton/food"
dst_directory = "H:/m/Sabaton/fav"

comb = combiner.Combiner(src_directory, dst_directory)
comb.combine()