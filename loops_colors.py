colors = ["red", "orange", "green", "violet", "blue", "yellow"]


def n_colors(colors, n=1):
    if n <= len(colors):
        return colors[:n]


def all_colors_compilation(colors_list):
    for i in range(len(colors_list)):
        print(n_colors(colors_list, i+1))


print(n_colors(colors, 2))
all_colors_compilation(colors)

corporation_description = """Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli"""
str_begin = corporation_description.find('(')
str_end = corporation_description.find(')')
print('korporacja:', corporation_description[str_begin+1: str_end])
