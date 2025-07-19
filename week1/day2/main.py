quote = input("Enter your favorite quote: ")
author = input("Who said it? ")

# Using f-string
print(f'"{quote}" - {author}')

# Using .format()
print('"{}" - {}'.format(quote, author))
