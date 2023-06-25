row1 = ["a","b","c"]
row2 = ["d","e","f"]
row3 = ["i","j","k"]
map = [row1,row2,row3]



number = input("Enter the row and column ")
horizontal = int(number[0])
vertical = int(number[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = "P"
print(f"{row1}\n{row2}\n{row3}")
