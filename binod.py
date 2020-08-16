import os
def isBinod(filename):
    with open(filename,"r")as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    dir_contents = os.listdir()
    nBinod=0
    # print(dir_contents)
    for item in dir_contents:
        if item.endswith("txt"):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            if(flag):
                print(f"**********Binod is found in {item}@@@@@@@@@@@@")
                nBinod +=1
            else:
                print(f"Binod not found in {item}")
    print("*******Binod Detecting summery******")
    print(f"{nBinod} files found with Binod hidden with them")









