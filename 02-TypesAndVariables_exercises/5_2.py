cube_side_string = input('Enter cube side: ')  # Pobiera długość boku sześcianu od użytkownika jako tekst (str)
cube_side = int(cube_side_string)    # Konwertuje tekst na liczbę całkowitą (int)

cube_volume = cube_side ** 3      # Oblicza objętość sześcianu ze wzoru V = a³
cube_surface_area = 6 * (cube_side ** 2)    # Oblicza pole powierzchni całkowitej ze wzoru Pc = 6 * a²

print(f'The volume of a cube with side {cube_side} is {cube_volume}')  # Wypisuje objętość sześcianu w f-stringu
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}') # Wypisuje pole powierzchni w f-stringu