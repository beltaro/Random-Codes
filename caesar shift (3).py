list = []
list_converted = []
mode  = input("Do You Want To Turn Numbers Into Characters Or The Opposite (n-c for num to chr or c-n for chr to num) : ")
if mode == "n-c":
    yes_or_no = input("Do You Have The Full Code (N for no Or Y for yes): ")
    if yes_or_no == "Y":
        print("Wip")
    if yes_or_no == "N":
        length = int(input("How Long Is Your Input : "))
        shift_amount = int(input("How Many Shifts Do You Want (make sure its the same amount when you try to decode this code): "))
        for i in range(length):
            list.append(int(input("Number : ")))
            list_converted.append(chr(list[i]-shift_amount))
        output_string = list_converted
        print("Your Sentence Is ", output_string)
    else:
        print("invalid input")
if mode == "c-n":
    yes_or_no = input("Do You Have The Full Code (N for no Or Y for yes): ")
    if yes_or_no == "Y":
        print("Wip")
    if yes_or_no == "N":
        length = int(input("How Long Is Your Input : "))
        shift_amount = int(input("How Many Shifts Do You Want (make sure its the same amount when you try to decode this code): "))
        for i in range(length):
            list.append(input("Input : "))
            list_converted.append(ord(list[i])+shift_amount)
        output_string = list_converted
        print("Your Code Is ", output_string)
    else:
        print("invalid input")
else:
    print("invalid input")
