from string import Template


def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    s = " This is a string "
    s2 = b.decode('utf-8')  # this is the correspond to asci
    print(s + s2)

    # change it to byte. Both are of the same datatype - to get concatenated byes
    b2 = s.encode('utf-8')
    print(b + b2)

    b3 = s.encode('utf-32')
    print(b3)
    s4 = b3.decode('utf-32')
    print("decoded b3 ==> " + s4)
    # Usual strig formattig with format()
    str1 = "you are watching {0} by {1}".format("Advanced Python", "Joe Marni")
    print(str1)

    # . Create a template with placeholders
    templ = Template("You are watching ${title} by ${author}")

    # 2 use the substitute method with keyward arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    # use the substitue method with dictionary

    data = {
        "author": "Joe Martin",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)
    if __name__ == "__main__":
        main()
