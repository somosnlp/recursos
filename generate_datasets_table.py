import pandas as pd

df = pd.read_csv("datasets.csv")
table_content = df.to_markdown(index=False)

with open("README.md", "r") as f:
    readme_content = f.read()

updated_readme_content = readme_content.replace("<!-- TABLE_CONTENT -->", table_content)

with open("README.md", "w") as f:
    f.write(updated_readme_content)
