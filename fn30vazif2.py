#Git ga ulash  muvaffaqiyatli bajarildi

from datetime import datetime, timedelta


foydalanuvchi_sana = input("Iltimos, sanani quyidagi formatda kiriting (YYYY-MM-DD HH:MM:SS): ")

try:
    sana_vaqt = datetime.strptime(foydalanuvchi_sana, "%Y-%m-%d %H:%M:%S")
    
    yangi_sana = sana_vaqt + timedelta(days=7, hours=3, minutes=15)

    formatlangan_sana = yangi_sana.strftime("%A, %d-%B-%Y %H:%M:%S")

    kunlar = {
        "Monday": "Dushanba",
        "Tuesday": "Seshanba",
        "Wednesday": "Chorshanba",
        "Thursday": "Payshanba",
        "Friday": "Juma",
        "Saturday": "Shanba",
        "Sunday": "Yakshanba",
    }

    oylar = {
        "January": "Yanvar",
        "February": "Fevral",
        "March": "Mart",
        "April": "Aprel",
        "May": "May",
        "June": "Iyun",
        "July": "Iyul",
        "August": "Avgust",
        "September": "Sentabr",
        "October": "Oktabr",
        "November": "Noyabr",
        "December": "Dekabr",
    }

    for ing_kun, uz_kun in kunlar.items():
        formatlangan_sana = formatlangan_sana.replace(ing_kun, uz_kun)

    for ing_oy, uz_oy in oylar.items():
        formatlangan_sana = formatlangan_sana.replace(ing_oy, uz_oy)

    print(formatlangan_sana)

except ValueError:
    print("Iltimos, sanani to'g'ri formatda kiriting.")

# kodni qo'shish amalga oshirildi