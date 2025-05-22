def word_count(text):
    words = text.lower().split()

    word_dict = {}
    for word in words:
        word = word.strip('.,!?;:()[]{}"\'')
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


text_input = "Сонце світить, сонце гріє. Сонце сяє на небі! Сонце, сонце — завжди сонце."

counts = word_count(text_input)

frequent_words = [word for word, count in counts.items() if count > 3]

print("Словник частот:", counts)
print("Слова, що зустрічаються більше 3 разів:", frequent_words)
