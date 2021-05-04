def statement_gen(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    above = decoration * len(statement)
    print(above)
    print(statement)
    print(above)
    return ""

for item in range(0, 3):
    statement = input("Statement: ")
    decoration = input("Decoration: ")
    statement_gen(statement, decoration)