from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horácio"]
houses = ["Grifinória", "Lufa-Lufa", "Corvinal", "Sonserina"]

symbols = []

knowledge = And()

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

# Cada pessoa pertence a uma casa.
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Grifinória"),
        Symbol(f"{person}Lufa-Lufa"),
        Symbol(f"{person}Corvinal"),
        Symbol(f"{person}Sonserina")
    ))

# Apenas uma casa por pessoa.
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
                )

# Apenas uma pessoa por casa.
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
                )

# TODO
# print(knowledge.formula())
knowledge.add(
    Or(Symbol('GilderoyGrifinória'), Symbol('GilderoyCorvinal'))
)

knowledge.add(
    Not(Symbol('PomonaSonserina'))
)

knowledge.add(
    Symbol('MinervaGrifinória')
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
