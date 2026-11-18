###
# Returns formatted time string in 24-hour or 12-hour format
#
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}' # :02d dopisuje zero, jeśli liczba jest jednocyfrowa (np. 8 - '08')
    
    elif time_format == '12':
        # Określamy przedrostek (am przed południem, pm od 12:00 w górę)
        if hours < 12:
            period = 'am'
        else:
            period = 'pm'
            
        # Przeliczamy godzinę na format 12-godzinny (północ 0 i południe 12 stają się 12)
        hour_12 = hours % 12
        if hour_12 == 0:
            hour_12 = 12
            
        # W formacie 12-godzinnym godzina nie ma zera (np. '7:30am'), a minuty mają (:02d)
        return f'{hour_12}:{minutes:02d}{period}'

# Testowanie funkcji dla wszystkich podanych przypadków
print(time_string(15, 38, '24'))  # '15:38'
print(time_string(8, 3, '24'))    # '08:03'
print(time_string(0, 5, '24'))    # '00:05'
print(time_string(11, 15, '12'))  # '11:15am'
print(time_string(0, 7, '12'))    # '12:07am'
print(time_string(7, 30, '12'))   # '7:30am'
print(time_string(12, 46, '12'))  # '12:46pm'
print(time_string(13, 10, '12'))  # '1:10pm'
print(time_string(19, 2, '12'))   # '7:02pm'