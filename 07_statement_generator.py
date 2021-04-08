def statement_gen(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    above = decoration * len(statement)
    print(above)
    print(statement)
    print(above)
    return ""

statement_gen("Higher Lower Game", "*")
