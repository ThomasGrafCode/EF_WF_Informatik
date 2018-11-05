def is_unique_email(names):
    for name in names:
        if names.count(name) > 1:
            return(False)
    return(True)