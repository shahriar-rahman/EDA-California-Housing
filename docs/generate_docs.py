import python_utils.common_utils as cu
input_path = "../dataset/interim/california_housing.csv"
save_path = "docs/data_dictionary.md"

df = cu.load_df("csv", "pd", input_path)
columns = [column for column in df.columns]

doc = ["## • Data Dictionary",
       "| features | dtype | mean value | standard deviation | min | max | description |",
       "| :-: | :-: | :-: | :-: | :-: | :-: | :-: |"]

for column in columns:
    try:
        descriptions = df.describe().loc[['mean', 'std', 'min', 'max']]
        doc.append(f'| {column} | {df[column].dtype} | {descriptions.at["mean", column]:.1f} | {descriptions.at["std", column]:.1f} | {descriptions.at["min", column]:.1f} | {descriptions.at["max", column]:.1f} |  |')

    except Exception as e:
        print(f"Exception: {e}")
        doc.append(f"| {column} | {df[column].dtype} | n/a | n/a | n/a | n/a |  |")

doc_str = "\n".join(doc)
with open(save_path, "w+") as file:
    file.write(doc_str)
