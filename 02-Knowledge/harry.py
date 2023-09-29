from logic import *

rain = Symbol("rain")  # Está chovendo
hagrid = Symbol("hagrid")  # Harry vai visitar Hagrid
dumbledore = Symbol("dumbledore")  # Harry vai visitar Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

# print(knowledge.formula())
print(model_check(knowledge, rain))
