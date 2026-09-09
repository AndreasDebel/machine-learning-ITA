def main() -> None:
    number = askNo()
    checkNo(number)

def askNo() -> int:
    number = int(input("Write a number: "))
    return number
    
def checkNo(number: int) -> None:
    if (number >= 3):
        print("Hello World!")
        


if __name__ == "__main__":
    main()