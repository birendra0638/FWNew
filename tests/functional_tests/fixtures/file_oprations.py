
def test_flat_file():
    file1 = open("xyz.txt", "w+")
    file1.write("heyyyy")
    line = input("Enter a line")
    file1.writelines(line.split('.'))
    file1.writelines(["\nSee you soon!", "\nOver and out."])
    file1.writelines(["\nSee you soon!", "\nOver and out."])
    file1.writelines(["\nSee you soon!", "\nOver and out."])
    file1.writelines(["\nSee you soon!", "\nOver and out."])
    file1.close()

    f = open("xyz.txt", "r+")
    print(f.read())

    f.close()

def test_csv_file():
    pass

def test_excel_file():
    file = ''