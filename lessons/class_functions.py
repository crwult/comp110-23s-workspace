def find_courses(cs: list[Courses]) -> list[str]:
    new_list: list[str] = []
    for elem in cs:
        if elem.level >= 400:
            for preq in elem.prerequisites:
                if elem.name == preq:
                    new_list.append(preq)