
def parser (csv):
    f = open(csv, "r")
    lines = f.readlines()
    lines = lines[1:]
    f.close()
    infoDict = dict()
    #_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
    infoDict["id"] = []
    infoDict["index"] = []
    infoDict["dataEMD"] = []
    infoDict["n_1"] = []
    infoDict["n_2"] = []
    infoDict["idade"] = []
    infoDict["genero"] = []
    infoDict["morada"] = []
    infoDict["modalidade"] = []
    infoDict["clube"] = []
    infoDict["email"] = []
    infoDict["federado"] = []
    infoDict["resultado"] = []

    for line in lines:
        line = line.split(",")
        infoDict["id"].append(line[0])
        infoDict["index"].append(line[1])
        infoDict["dataEMD"].append(line[2])
        infoDict["n_1"].append(line[3])
        infoDict["n_2"].append(line[4])
        infoDict["idade"].append(line[5])
        infoDict["genero"].append(line[6])
        infoDict["morada"].append(line[7])
        infoDict["modalidade"].append(line[8])
        infoDict["clube"].append(line[9])
        infoDict["email"].append(line[10])
        infoDict["federado"].append(line[11])
        infoDict["resultado"].append(line[12].strip())

    return infoDict

def sort_modalidades (infoDict):
    modalidades = []
    for modalidade in infoDict["modalidade"]:
        if modalidade not in modalidades:
            modalidades.append(modalidade)
    modalidades.sort()
    return modalidades


def atletas_aptos (infoDict):
    aptos = 0
    n_aptos = 0
    total = 0
    for res in infoDict["resultado"]:
        total +=1
        if res in "true":
            aptos +=1
        else:
            n_aptos +=1
    return (aptos/total * 100, n_aptos/total * 100)


def find_age_range(age):
    if age < 20 or age > 100:
        return "Age out of range"
    lower_bound = (age // 5) * 5
    upper_bound = lower_bound + 4
    return f"[{lower_bound}-{upper_bound}]"


def range_distribuicao(infoDict):
    rangeDict = dict()
    for age in infoDict["idade"]:
        age = int(age)
        range_ = find_age_range(age)
        if range_ in rangeDict:
            rangeDict[range_] += 1
        else:
            rangeDict[range_] = 1
    return rangeDict
    


dictInfo = parser("emd.csv")
l_modalidades = sort_modalidades(dictInfo)

print(f"Modalidades: {l_modalidades}")

ap, n_ap = atletas_aptos(dictInfo)

print(f"Percentagem de atletas aptos: {ap}%")
print(f"Percentagem de atletas não aptos: {n_ap}%")

distribuicao = range_distribuicao(dictInfo)

print("Distribuição de idades:")
for key in distribuicao:
    print(f"{key}: {distribuicao[key]}")




