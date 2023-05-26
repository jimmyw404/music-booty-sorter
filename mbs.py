import os
import combiner

src_directory = "H:/m/Powerwolf/test"
dst_directory = "H:/m/Powerwolf/test_fav"

comb = combiner.Combiner(src_directory, dst_directory)
comb.combine()