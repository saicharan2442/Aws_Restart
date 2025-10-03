import jsonFileHandler

data = jsonFileHandler.readJsonFile('insulin.json')

if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    print("bInsulin: " + bInsulin)
    print("aInsulin: " + aInsulin)
    print("molecularWeightInsulinActual: " + str(molecularWeightInsulinActual))

    aaWeights = data['weights']
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights}
    molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaCountInsulin)

    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    percent_error = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
    print("Percent error: " + str(percent_error))
else:
    print("Error. Exiting program")
