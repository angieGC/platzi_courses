def read():
    numbers = []
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Angie", "Catalina", "Ana", "Joaquina", "Paola", "Alexandra"]
    with open("./archivos/names.txt","w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def write_add():
    names = ["Carlos", "Alberto", "Fernando", "Joaquin", "Hector", "Alejandro", "Daniel"]
    with open("./archivos/names.txt","a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()

if __name__ == "__main__":
    run()
