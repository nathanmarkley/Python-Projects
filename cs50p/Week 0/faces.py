#convert text emoji to picture emoji
def convert(text):
    t = text.split( " ")
    emojis = {
        ":)" : "🙂",
        ":(" : "🙁"
    }
    n = " "
    for a in t:
        n += emojis.get(a, a) + " "
    return n

#ask user for a emoji in text and call convert
#and print emoji to screen
def main():
    text = input("Enter a happy face or a sad face in text: ")
    print(convert(text))

main()