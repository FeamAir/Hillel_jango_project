def qs2html(gr):
    lst = []
    if gr is not None:
        for line in gr:
            lst.append(str(line))
    else:
        lst.append("QuerySet is empty")

    return "<br>".join(lst)
