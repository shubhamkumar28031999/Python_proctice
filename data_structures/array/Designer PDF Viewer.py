def designerPdfViewer(h, word):
    max_height=0
    l=len(word)
    for i in range(l):
        max_height=max(max_height,h[ord(word[i])-97])
    return l*max_height

if __name__=="__main__":
    word='abc'
    h=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    print(designerPdfViewer(h,word))