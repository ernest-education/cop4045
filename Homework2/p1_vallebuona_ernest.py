def line_number(input_file: str, output_file: str )-> None:
    """read a text file and record each line alongside a line number"""
    try:
        with open(input_file, "r") as fin:
            with open(output_file, "w") as fout:
                num = 1
                for line in fin:
                    fout.write(str(num) + ". " + line)
                    num += 1
    except Exception as fail:
        print("Something went wrong while numbering the lines: ")
        raise fail

def parse_functions(thefile: str) -> tuple:
    """read a Python file and give information about functions within it"""
    try:
        with open(thefile, "r") as file:
            lines = file.readlines()

        functions = []
        i=0

        while i < len(lines):
            line = lines[i]

            #find def
            if line.startswith("def "):
                #name
                defstart = 4
                defend = line.find("(")
                name = line[defstart:defend]

                #find args
                argstart = line.find("(") + 1
                argend = line.find(")")
                arguments = line[argstart:argend]

                code = line
                i += 1

                while i < len(lines):
                    nextline = lines[i]
                    if nextline.startswith("def "):
                        break #new function detected
                    if nextline.strip() != "":
                        #no comments
                        if not nextline.lstrip().startswith("#"):
                            code += nextline
                    i += 1

                line_number = i - code.count("\n") + 1
                #dont count whitespace in lines

                functions.append((line_number, arguments, code))

                continue

            i += 1

        #sort em alphabetically by function 
        functions.sort(key=lambda x: x[1])

        return tuple(functions)
    except Exception as fail:
        print("Something went wrong while parsing the python code")
        raise fail


def main() -> None:
    "test that stuff homie"

    line_number("p1test.py", "p1testnumbered.txt")
    final = parse_functions("p1test.py")

    print(final)

if __name__ == "__main__":
    main()