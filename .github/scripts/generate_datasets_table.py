import pandas as pd

df = pd.read_csv("datasets.csv")

# Sort the DataFrame by the "nombre" column and save it
df.sort_values(by="nombre", inplace=True)
df.to_csv("datasets.csv", index=False)

# Generate the datasets table
table_content = df.to_markdown(index=False)

with open("README.md", "r") as f:
    readme_template = f.read()

start_delimiter = "<!-- START_TABLE_CONTENT -->"
end_delimiter = "<!-- END_TABLE_CONTENT -->"

start_pos = readme_template.find(start_delimiter)
end_pos = readme_template.find(end_delimiter)

updated_readme_content = (
    readme_template[:start_pos + len(start_delimiter)]
    + "\n" + table_content + "\n"
    + readme_template[end_pos:]
)

with open("README.md", "w") as f:
    f.write(updated_readme_content)
