# Визначення класів з обробниками повідомлень
class With_land:
    def house_view(self):
        return "Це будинок земельною ділянкою."


class Without_land:
    def house_view(self):
        return "Це будинок без земельної ділянки."


class For_many_families:
    def house_view(self):
        return "Це будинок для багатьох сімей."


class For_one_family:
    def house_view(self):
        return "Це будинок для однієї сім'ї."


class Villets:
    def house_view(self):
        return "Це великий будинок з власною земельною ділянкою."


class Apartmens:
    def house_view(self):
        return "Це квартирний будинок з власними апартаментами."


# Функція для виклику обробників повідомлень
def message_handler(house):
    print(house.house_view())


with_land_house = With_land()
without_land_house = Without_land()
for_many_families_house = For_many_families()
for_one_family_house = For_one_family()

villets_house = Villets()
apartmens_house = Apartmens()

print("Для класу 'Villets':")
message_handler(villets_house)

print("\nДля класу 'Apartmens':")
message_handler(apartmens_house)

