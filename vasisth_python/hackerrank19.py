if __name__ == '__main__':
    s = list(input())
    print(any([v.isalnum() for v in s]))
