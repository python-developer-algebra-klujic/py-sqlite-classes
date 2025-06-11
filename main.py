# START
from cake_repo import (CakesRepo,
                       create_table,
                       insert_into,
                       get_cakes,
                       get_cake_by_id)


cakes_repo = CakesRepo()
cakes = cakes_repo.get_cakes()
# END

create_table()


# BEFORE GET CAKES
# for cake in cakes:
#     print(cake)
#     insert_into(cake)


# AFTER GET CAKES
cakes = get_cakes()
for cake in cakes:
    print(cake)


cake_by_id = get_cake_by_id(2)
print()
print(cake_by_id)
print()
