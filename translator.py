import emoji

x = ""
dict = {
    "mad" : "😡",
    "dog" : "🐶",



}
while True:
    s = input()
    for word in s.split():
        print(word)
        if word in dict:
            x = x + dict[word]


    print(x)
