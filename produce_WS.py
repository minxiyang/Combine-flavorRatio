from func.produceWS import produceWS


def main():
    for cut in range(500, 501, 100):
        produceWS(cut)

if __name__=="__main__":
    main()



