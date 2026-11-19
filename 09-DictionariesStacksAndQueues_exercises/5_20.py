# Program zapisuje rozbudowany, zagnieżdżony słownik z kartą pacjenta
# do pliku patient.json z czytelnym wcięciem (indent=4).

import json

def main():
    # Zagnieżdżony słownik łączący tekst, listy (alergie, leki) oraz kolejne słowniki (adres, operacje)
    data = {
        "patient_record": {
            "patient_id": "P001234",
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "1985-05-15",
            "gender": "Male",
            "contact_info": {
                "phone_number": "+1-555-123-4567",
                "email": "johndoe@example.com",
                "address": {
                    "street": "123 Main St",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10001",
                    "country": "USA"
                }
            },
            "medical_history": {
                "allergies": ["Penicillin", "Peanuts"],
                "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
                "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
                "surgeries": [
                    {
                        "surgery_type": "Appendectomy",
                        "date": "2015-08-20"
                    }
                ]
            }
        }
    }

    file_name = "09-DictionariesStacksAndQueues_exercises/patient.json"

    # Tryb 'w' tworzy nowy plik (lub nadpisuje istniejący), a indent=4 formatuje strukturę z wcięciami
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print("Data has been written to", file_name)

if __name__ == "__main__":
    main()