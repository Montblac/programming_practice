"""
Programming Praxis | Perfect Shuffle
March 13, 2020

A perfect shuffle, also known as a faro shuffle, splits a deck of cards into equal halves (there must be an even number 
of cards), then perfectly interleaves them. Eventually a series of perfect shuffles returns a deck to its original 
order. For instance, with a deck of 8 cards named (1 2 3 4 5 6 7 8), the first shuffle rearranges the cards to (1 5 2 6 
3 7 4 8), the second shuffle rearranges the cards to (1 3 5 7 2 4 6 8), and the third shuffle restores the original 
order (1 2 3 4 5 6 7 8).

Your task is to write a program that performs a perfect shuffle and use it to determine how many perfect shuffles are 
required to return an n-card deck to its original order; how many perfect shuffles are required for a standard 52-card 
deck? When you are finished, you are welcome to read or run a suggested solution, or to post your own solution or 
discuss the exercise in the comments below.
"""


def shuffle(deck, mid):
    """ Performs a perfect shuffle on the deck
    """
    left, right = deck[:mid], deck[mid:]
    shuffled = []
    for a, b in zip(left, right):
        shuffled.append(a)
        shuffled.append(b)
    return shuffled


if __name__ == '__main__':
    while True:
        try:
            size = input("How many cards in a deck? ")
            if not size.isdigit() or int(size) % 2 != 0:
                raise ValueError
        except ValueError:
            print("Invalid input: Please enter an even integer!")
        else:
            break

    deck = [c for c in range(int(size))]
    mid = len(deck) // 2
    result = deck
    count = 0
    while result != deck or count <= 0:
        result = shuffle(result, mid)
        count += 1

    print('Shuffles needed: {}'.format(count))
