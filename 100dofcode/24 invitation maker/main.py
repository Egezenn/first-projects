def getbase(baseletterfile):
    with open(baseletterfile) as base:
        return base.read()


def getnames(namesfile):
    namelist = []
    with open(namesfile) as names:
        for line in names:  # {filename}.readlines() actually does what this for loop does, except deleting line breaks
            modified_line = line.replace("\n", "")  # {filename}.strip() can be used to delete spaces or line breaks
            namelist.append(modified_line)
    return namelist


letter_base = getbase("Input/Letters/starting_letter.txt")
names_to_be_used = getnames("Input/Names/invited_names.txt")

for name in names_to_be_used:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="x") as letter:
        letter.write(letter_base.replace("[name]", f"{name}"))
