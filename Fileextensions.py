File=input("Enter the file name:")
a=File.find(".")
dict={"py":"python", "txt":"text", "c":"C"}
b=str(File[a+1:])
ext=dict[b]
print("The extension of the file is:",ext)
