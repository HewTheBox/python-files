row1 = ["a","b","c"]
row2 = ["d","e","f"]
row3 = ["g","h","i"]

map = [row1,row2,row3]

position = input("Enter the row and column?\n:=>")
row = int(position[0])
column = int(position[1])

map[column -1][row -1] = "X"

print(f"{row1}\n{row2}\n{row3}")
