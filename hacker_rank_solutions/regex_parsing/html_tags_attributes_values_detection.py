from html.parser import HTMLParser


class parseHTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

N = int(input())
parser = parseHTML()


for i in range(N):
    i = input()
    parser.feed(i)