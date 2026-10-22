def main() -> None:
    number = askNo()
    checkNo(number)

def askNo() -> int:
    number = int(input("Write a number: "))
    return number
    
def checkNo(number: int) -> None:
    if (number >= 3):
        print("Your no. is higher than 3, otherwise nothing would happen.")
        


if __name__ == "__main__":
    main()