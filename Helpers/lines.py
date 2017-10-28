with open("subjects_ham.txt", "a") as subjects_file:
    with open("ham_utf.txt") as ham_file:
        for line in ham_file:
            if "Subject" in line:
                if not "=?Shift" in line and not "=?ISO" in line and not "lists-" in line and not "=?UTF" in line:
                    subjects_file.write(line)
                    