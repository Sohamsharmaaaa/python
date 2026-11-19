# Write a program to accept the filename, check the extension of it and show the appropriate warning message
filename = input("Enter the filename:: ")
ext = filename.split(".")
if len(ext) != 2:
    print("Wrong Filename")
else:
    match ext[1]:
        case "exe" | "out":
            print("this ia an executable file")
        case "txt":
            print("This is a text file")
        case "pdf":
            print("This is a pdf file")
        case "ppt":
            print("This is a ppt")
        case "docx":
            print("this is a document")
        case "py":
            print("Ths is apython file")
        case _:
            print("Unknown filename")
