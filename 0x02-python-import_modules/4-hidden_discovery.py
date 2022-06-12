#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    fetch_dir = dir(hidden_4)
    for i in fetch_dir:
        if i[:2] != "_":
            print("{:s}".format(i))
