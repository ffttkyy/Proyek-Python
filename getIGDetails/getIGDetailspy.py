import instaloader

#creating object
ig = instaloader.Instaloader()

#taking the instgram username as input form user
print("\nProgram cek Details IG\n")
username = input("Masukan Username : ")

#Fetching the details username using instloader object
profile = instaloader.Profile.from_username(ig.context, username)

#printing the details of provided and storing the profile pic the account
print("Username : ", profile.username)
print("Jumlah postingan yang di Upload : ", profile.mediacount)
print(profile.username+" Mempunyai " + str(profile.followers)+ ' followers.')
print(profile.username+" Mengikuti " + str(profile.followees)+ ' people')
print("Bio : ", profile.biography)
instaloader.Instaloader().download_profile(username,profile_pic_only=True)