import instaloader

loader = instaloader.Instaloader()
loader.login("gramsleuth4", "BigNut123")

target = str(input("Target Username: "))

profile = instaloader.Profile.from_username(loader.context, target)
followers = profile.get_followers()
followees = profile.get_followees()

for follower in followers:
    print(follower)
print()
for followee in followees:
    print(followee)
