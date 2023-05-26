import os
import combiner

src_directory = "H:/m/Windrose/favfood"
dst_directory = "H:/m/Windrose/_fav"

comb = combiner.Combiner(src_directory, dst_directory)
comb.combine()