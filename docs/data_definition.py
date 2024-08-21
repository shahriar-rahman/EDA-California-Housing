import python_utils.common_utils as cu
from sklearn.datasets import fetch_california_housing

# Fetch the California housing dataset
sklearn_data = fetch_california_housing()
save_path = "docs/data_definition.md"

data_def = sklearn_data['DESCR'][200:1420]

doc = ["## • Data Definition"]

try:
    doc.append(data_def)

except Exception as e:
    print(f"Exception: {e}")


doc_str = "\n".join(doc)
with open(save_path, "w+") as file:
    file.write(doc_str)
