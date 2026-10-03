def convert_seconds():
    print("welcome to time converter(:")
    given_seconds = int(input("enter the duration in seconds: "))
    
    converted_hours = given_seconds // 3600
    converted_minutes = (given_seconds % 3600) // 60
    convert_seconds = given_seconds % 60
    
    print(f"the duration is: {converted_hours} hours, {converted_minutes} minutes, {convert_seconds} seconds.")

if __name__ == "__main__":
    convert_seconds()
