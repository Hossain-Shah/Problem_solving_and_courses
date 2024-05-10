english_subscrubers = input()
english_subscrubers_list = input().split()

french_subscrubers = input()
french_subscrubers_list = input().split()

print(len(set(english_subscrubers_list) - set(french_subscrubers_list)))