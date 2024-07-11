def yoda_speak():
    while True:
        sentence = input("Enter a sentence (enter '0' to terminate): ")
        if sentence == '0':
            print("Exiting program...")
            break
        words = sentence.split()
        yoda_sentence = ' '.join(reversed(words))
        print(yoda_sentence)

# Example usage:
yoda_speak()
