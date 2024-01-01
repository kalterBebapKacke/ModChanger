def getLCIndes(List:list):
    for x in range(len(List)):
        String = List[x]
        if String == 'Lethal Company':
            return x
    return -1

def writeLog(Message:str):
    with open("log.txt", 'w') as f:
        f.write(Message)

def getPath(List:list):
    newPath = [x for x in List]
    del newPath[len(newPath)-1]
    return newPath