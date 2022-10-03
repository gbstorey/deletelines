import pandas as pd
trial_names = ["50 degrees"]
for name in trial_names:
    data = pd.read_csv(f"{name}.csv", names=['time', 'absorbance'])
    to_remove = []
    for item in range(0, data.shape[0]):
        if data['absorbance'][item] == " ":
            to_remove.append(item)
    reformed_data = data.drop(to_remove)
    reformed_data = reformed_data.dropna()
    print(reformed_data)
    reformed_data.to_csv(f"{name} reformed.csv", index=False, header=None)
