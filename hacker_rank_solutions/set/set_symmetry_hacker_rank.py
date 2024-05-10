english_subscribers = input()
english_subscribers_list = input().split()

french_subscribers = input()
french_subscribers_list = input().split()

print(len(set(english_subscribers_list) ^ set(french_subscribers_list)))