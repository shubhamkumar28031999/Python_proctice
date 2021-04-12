square={num:num**2 for num in range(1,11)}
print(square)
square1={f"square of {num} is ":num**2 for num in range(1,11)}
print(square1)
for k,v in square1.items():
    print(f"{k}:{v}")

name="shubham"
word_count={char:name.count(char) for char in name}
print(word_count)