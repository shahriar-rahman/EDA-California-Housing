import python_utils.common_utils as cu
import io
input_path = "../dataset/interim/california_housing.csv"
save_path = "docs/data_info.md"

df = cu.load_df("csv", "pd", input_path)

# Create a buffer to hold the info output
buffer = io.StringIO()

# Capture the output of df.info() into the buffer
df.info(buf=buffer)

# Get the content of the buffer as a string
info_str = buffer.getvalue()

# Write the string to a text file
with open(save_path, "w") as file:
    file.write(info_str)

