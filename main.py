# Pull names into a list
with open("input/names/invited_names.txt") as data_names:
    names = data_names.readlines()

# Pull letter template and read (convert to string)
with open("input/letters/starting_letter.txt") as starting_letter:
    model = starting_letter.read()

# Formats list names and creates a letter file for each name
    for i in range(len(names)):
        names[i] = names[i].strip()
        model_formatted = model.replace("[name]", f"{names[i]}")
        with open(f"./output/ready-to-Send/letter{str(i)}.txt", "w") as new_letter:
            new_letter.write(model_formatted)
