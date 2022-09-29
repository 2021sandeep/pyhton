def Back_to_home(string):
    string=string
    x=[i for a,i in enumerate(string)]
    if x.count("N")==x.count("S")==x.count("E")==x.count("W"):
        return True
    else:
        return False
