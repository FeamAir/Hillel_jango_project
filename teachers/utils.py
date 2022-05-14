def qs2html(tc):
    lst = []
    if tc is not None:
        for line in tc:
            lst.append(str(line))
    else:
        lst.append("QuerySet is empty")

    return "<br>".join(lst)
