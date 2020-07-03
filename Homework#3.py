Cough = "Dry"
Temperature = "38"
Feeling = "Feverish"
COVID_19 = False

if Cough == "Wet" and Temperature == "37" and Feeling == "Feverish":
    COVID_19 = True     
print(COVID_19)


if Cough == "Dry" and Temperature == "38" and Feeling == "Feverish":
    COVID_19 = True
print(COVID_19)

if Cough == "Dry" and Temperature == "38" or Feeling == "Normal":
    COVID_19 = True
print(COVID_19)



    