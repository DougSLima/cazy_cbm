import pandas as pd

def add_line_break(text, row_width=80):
    parts = []
    for i in range(0, len(text), row_width):
        parts.append(text[i:i + row_width])
    return '\n'.join(parts)


cazy_df = pd.read_csv(r'C:\\Users\\Maninho\\Desktop\\CAZY\\cazy_df.csv', header=True, sep=';')

with open(r'C:\\Users\\Maninho\\Desktop\\CAZY\\cazy_df.fasta', 'a') as f:
    for index, row in cazy_df.iterrows():
        f.write(f">{row['Title']}\n{add_line_break(row['Sequences'])}")
f.close()