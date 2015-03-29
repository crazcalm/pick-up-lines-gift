TABLE = {"\xe2\x80\x99s": "?"}


def format_line(index, line):
    line = line.replace("\xe2\x80\xa2", "")
    line = line.replace("\xe2\x80\x99s", "?")
    line = line.replace("\xe2\x80\x99", "'")
    line = line.replace("\xe2\x80\x94", "-")
    line = line.replace("\xe2\x80\xa6", "...")

    line = line.replace("\xe2\x80\x9c", '"')
    line = line.replace("\xe2\x80\x9d", '"')
    line = line.strip()
    print(index)
    print(line)

    return line


def get_file_content(file, limit=False):
    results = []
    comment = ""
    with open(file, "r") as f:
        for index, line in enumerate(f.readlines()):
            #print("original line: ", line)
            if line.strip().startswith("\xe2\x80\xa2"):
                # Need to replace all the strange characters
                test = comment.replace("\xe2\x80\x99s", "?")
                test = test.replace("\xe2\x80\x99", "'")
                #print("test: ", test)
                #print("comment: ", comment)
                results.append(comment)
                #print("len(results):", len(results))
                comment = line.strip()[:]
            else:
                #print("Partial line: ", line.strip())
                comment = comment.strip() + " " + line.strip()

            if limit:
                if index > limit:
                    break
    return results


def get_pickup_lines_and_comebacks(content):
    pickup_lines = []
    comebacks = []
    transition = False

    for index, item in enumerate(content):
        #print(item)
        if "Suggestions for women responding to pick-up lines:" in item:
            line = item.replace("Suggestions for women responding to pick-up lines:", "").strip()
            line = format_line(index, line)
            pickup_lines.append(line)
            transition = True
        elif item.startswith("\xe2\x80\xa2") and not transition:
            item = format_line(index, item)
            #print("pickupline: ", item)
            pickup_lines.append(item)
        elif item.strip().startswith("\xe2\x80\xa2") and transition:
            item = format_line(index, item)
            #print("comeback: ", item)
            comebacks.append(item)
    return pickup_lines, comebacks


if __name__ == "__main__":
    content = get_file_content("practice.txt")
    print("len(content): ", len(content))
    for index, item in enumerate(content):
        if item.startswith("\xe2\x80\xa2"):
            #print(str(index) + ": " + item)
            #print(str(index), format_line(index, item))
            pass
        if "Suggestions for women responding to" in item:
            print(str(index) + ": " + item)
            test = item.replace("Suggestions for women responding to pick-up lines:", "").strip()
            #print("last pickup line: ", test)

    pickuplines, comebacks = get_pickup_lines_and_comebacks(content)
    print("len(pickuplines):", len(pickuplines))
    print("len(comeboacks):", len(comebacks))
    for line in comebacks:
        #print("line: ", line)
        pass