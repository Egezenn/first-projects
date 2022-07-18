try:
    file = open("the_file.txt")
    dic = {"key": "keyofthevalue"}
    print(dic["boo"])

except FileNotFoundError as error_file:
    print(f"{error_file}, created the file required!")
    file = open("the_file.txt", "w")

except KeyError as error_message:
    print(f"no key named {error_message}!")

else:
    content = file.read()
    print(content)

finally:
    with open("the_file.txt", "a") as final_file:
        final_file.write("file opened some time ago\n")
    file.close()

    raise KeyError("lul")
