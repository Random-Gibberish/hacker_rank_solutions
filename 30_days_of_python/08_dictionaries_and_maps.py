
def find_phone_number(query, phone_book):
    """ Returns the 'query's' phone number """

    phone_number = phone_book.get(query)

    try:
        print(query + '=' + phone_number)
    except TypeError:
        print('Not found')


if __name__ == '__main__':
    n = int(input().strip())    # Number of entry
    book = {}                   # Phone book

    for _ in range(n):                  # Add phone book entries
        entry = input().strip().split()
        book[entry[0]] = entry[1]

    queries = input().strip()   # Search for queries in phonebook

    while queries:
        find_phone_number(queries, book)
        queries = input().strip()
