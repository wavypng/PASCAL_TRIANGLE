from Rigoberto_Hinojos_PascalTriangle import Rigoberto_Hinojos_PascalTriangle

def main():
    
    line = ("-------------------------------------")

    pasOne = Rigoberto_Hinojos_PascalTriangle()

    print("Enter Size of Pascal Triangle you would like: ")
    num = int(input())
    pasOne.pascal(num)

    print("\n"+line)

    print("\nEnter row to choose from: ")
    n = int(input())
    print("\nEnter coulumn to choose from: ")
    k = int(input())
    print(line)
    print("\n Searching for....... C(" +str(n) +","+ str(k) +")\n")   

    pasOne.getChoices(n,k)



if __name__ == '__main__':
    main()