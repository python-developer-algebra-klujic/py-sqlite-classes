# START
from cake_repo import CakesRepo


cakes_repo = CakesRepo()
cakes = cakes_repo.get_cakes()
# END


for cake in cakes:
    print(cake)
