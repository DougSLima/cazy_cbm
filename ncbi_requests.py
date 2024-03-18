from eutils import Client
import pandas as pd
#Set api key
ec = Client(api_key='a5f3ff9a50469b812685039e84baf0e68e08')

#Get genbank acession list from file
lines_df = pd.read_csv(r'C:\\Users\\Maninho\\Desktop\\CAZY\\genbank_ids.txt', header=None, names=['genbank_acession'])
lines = lines_df['genbank_acession'].values

titles = []
genbank_acession_versions = []
genbank_ids = []
sequences = []

for genbank_acession in lines:
    try:    
        #Add genbank acession to list
        genbank_acession_versions.append(genbank_acession)
        #Fetch genbank id by genbank acession and add to list
        esr = ec.esearch(db='protein',term=genbank_acession)
        genbank_ids.append(esr.ids[0])
        #Fetch protein sequence by genbank id and add to list
        egs = ec.efetch(db='protein', id=esr.ids[0])
        eg = egs.gbseqs
        sequences.append(eg[0].sequence)
        #Fetch protein title
        titles.append(eg[0].definition)
    except:
        with open(r'C:\\Users\\Maninho\\Desktop\\CAZY\\genbank_id_exceptions.txt', 'a') as f:
            f.write(f"{genbank_acession}\n")

#Turn data into dataframe and write to file
cazy_dict = {'Title': titles, 'Genbank acession': genbank_acession_versions, 'Genbank ID': genbank_ids, 'Sequences': sequences}
cazy_df = pd.DataFrame(data = cazy_dict)

cazy_df.to_csv(r'C:\\Users\\Maninho\\Desktop\\CAZY\\cazy_df.csv', header=True, sep=';')