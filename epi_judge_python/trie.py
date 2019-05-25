class Node:
  def __init__(self, end_of_word=False):
    self.children = dict()
    self.end_of_word = end_of_word

def insert(trie, word):
  if word is None:
    return trie

  if trie is None:
    trie = Node()

  iterator = trie
  for character in word:
    if character not in iterator.children:
      iterator.children[character] = Node()

    iterator = iterator.children[character]

  iterator.end_of_word = True
  return trie

if __name__ == "__main__":
  #dictionary = ["word", "be", "cut"]
  dictionary = {"dog", "be", "cut", "car"}
  trie = None
  for word in dictionary:
    trie = insert(trie, word)

  iterator, i = trie, 0
  while i < len("cat"):
    character = "cat"[i]
    if character in iterator.children:
      iterator = iterator.children[character]
      i += 1
    else:
      break

  print("cat"[:i+1])
