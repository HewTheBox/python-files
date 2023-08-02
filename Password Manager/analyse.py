import pandas

data = pandas.read_csv("data.csv")

email = [row.email for (index, row) in data.iterrows()]

def view_passwords():
    return data
def wipe_sheet():
    with open("data.csv", mode="w") as file:
        file.write("website,email,password\n")
        
        
new = view_passwords()
print(new)