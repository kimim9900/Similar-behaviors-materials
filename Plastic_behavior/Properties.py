import pandas as pd
Plastic_properties = {
    "Grain Sieze": [6000],
    "Compressive Strength": [4.00, 15.0, 18.0, 25.0],
    "Maximum Service": [1600]
}

df = pd.DataFrame(Plastic_properties)

print(df)

