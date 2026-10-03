def generate_channel_name():
    print("welcome to you youtube channel generator(:")
    nick_name = input("what's your nickname: ").strip()
    channel_subject = input("what's your channel about: ").lower()
    print(f"you could name your channel ({channel_subject} with {nick_name})")

if __name__ == "__main__":
    generate_channel_name()
