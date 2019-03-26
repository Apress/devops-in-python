with open("important.tmp", "w") as fout:
    fout.write("The horse raced past the barn")
    fout.write("fell.\n")
os.rename("important.tmp", "important")