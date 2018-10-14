import matplotlib.pyplot as plt

# A CSV fájl sorainak beolvasása és tördelése a szeparál karakterek mentén.
lines = [line.strip().split(",") for line in open("Pokemon.csv", "r").readlines()]

# A pokémonok adatainak tárolására szolgáló lista. Minden pokémont kulcs-érték párokkal fogunk tárolni.
pokemons = []

# A kulcs-érték párok felvétele a pokemons listába. Az 1-es indextől indulunk, mert az első (0.) helyen a fejléc található.
for i in range(1, len(lines)):
    pokemons.append({lines[0][j]:lines[i][j] for j in range(len(lines[0]))})

# Támadási és védekezési értékek vizualizálása a legendás és nem legendás pokémonok esetén.
for pokemon in pokemons:
    if pokemon["Legendary"] == "True":
        plt.plot(int(pokemon["Attack"]), int(pokemon["Defense"]), "rD")
    else:
        plt.plot(int(pokemon["Attack"]), int(pokemon["Defense"]), "b^")
plt.show()

# Azon vizi pokémonok neveit tartalmazó tuple, melyek sebessége 100 és 150 közé esik.
water_pokemons = tuple(pokemon["Name"] for pokemon in pokemons if pokemon["Type 1"] == "Water" and 100 <= int(pokemon["Speed"]) <= 150)

# Az előzőleg kiszűrt nevek megjelenítése szóközzel elválasztva.
for pokemon in water_pokemons:
    print(pokemon, end=" ")

# Elsődleges típus szerint csoportosított pokémonok tárolására létrehozott szótár.
pokemons_by_type1 = {}

# A szótár feltöltése a megfelelő listákkal.
for pokemon in pokemons:
    ptype = pokemon["Type 1"]
    # Ha nincs még lista a vizsgált típushoz, akkor létrehoz egy újat.
    if not ptype in pokemons_by_type1:
        pokemons_by_type1[ptype] = []
    # Aktuális pokémon nevének felvétele a megfelelő listába.
    pokemons_by_type1[ptype].append(pokemon["Name"])

# Az egyes pokémon típusok darabszámának vizualizálása.
for pokemon in pokemons_by_type1:
    plt.barh(pokemon, len(pokemons_by_type1[pokemon]))
plt.show()
