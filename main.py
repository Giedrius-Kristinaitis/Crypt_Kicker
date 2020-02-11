from input import Input
from cypher import Cypher

data = Input()
data.populate_from_file("input.txt")

cypher = Cypher()
output = cypher.decypher(data, "the quick brown fox jumps over the lazy dog")

output.print_to_file("output.txt")
