import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()

                table = str.maketrans('', '', string.punctuation.replace('-', ''))
                content = content.translate(table)
                content = content.replace(' - ', ' ')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}
        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1
                positions[file_name] = position
            except ValueError:
                positions[file_name] = -1
        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)
        return counts


if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')

print(finder.get_all_words())

print(finder.find('TEXT'))

print(finder.count('teXT'))
