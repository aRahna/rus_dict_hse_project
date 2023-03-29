from backend import join_search_tables, join_search_conditions, search_query, load_page

query = [["head", "аминь"]]
print(len(search_query(join_search_tables(query), join_search_conditions(query))))
print("я нашел такие слова: ",(set(search_query(join_search_tables(query), join_search_conditions(query)))))
word = input("какое слово хотите изучить подробнее? просто скопируйте: ")
text = load_page(word)
with open("test.txt", "w", encoding="UTF-8") as f:
    for line in text:
        f.write(line)