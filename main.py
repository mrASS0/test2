meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
n = 5

for i in range(n):
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

    if parola in meme_dict.keys():
        print(meme_dict[parola])
    else:
        print("la parola che dici tu non la conosciamo")
