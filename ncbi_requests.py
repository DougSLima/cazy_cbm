from eutils import Client
import pandas as pd
#Set api key
ec = Client(api_key='a5f3ff9a50469b812685039e84baf0e68e08')

#Get genbank acession list from file
lines_df = pd.read_csv(r'C:\\Users\\Maninho\\Desktop\\CAZY\\genbank_cbms.txt', sep=";", header=None, names=['genbank_acession', 'CBM_family'])
lines = lines_df['genbank_acession'].values

titles = []
genbank_acession_versions = []
genbank_ids = []
sequences = []
families = []

for genbank_acession in lines:
    print(genbank_acession)
    try:    
        #Fetch genbank id by genbank acession
        esr = ec.esearch(db='protein',term=genbank_acession)
        genbank_id = esr.ids[0]
        
        #Fetch protein sequence by genbank id and add to list
        egs = ec.efetch(db='protein', id=esr.ids[0])
        eg = egs.gbseqs
        sequence = eg[0].sequence
        
        #Fetch protein title
        title = eg[0].definition

        #Fetch CBM family name
        family = lines_df.loc[lines_df['genbank_acession'] == genbank_acession]['CBM_family'].values[0]
    except:
        with open(r'C:\\Users\\Maninho\\Desktop\\CAZY\\genbank_id_exceptions_v3.txt', 'a') as f:
            f.write(f"{genbank_acession}\n")
    else:
        #Add genbank acession to list
        genbank_acession_versions.append(genbank_acession)
        #Add genbank id to list
        genbank_ids.append(genbank_id)
        #Add sequence to list
        sequences.append(sequence)
        #Add title to list
        titles.append(title)
        #Add CBM family name to list
        families.append(family)

#Turn data into dataframe and write to file
cazy_dict = {'Title': titles, 'Genbank acession': genbank_acession_versions, 'Genbank ID': genbank_ids, 'CBM_family': families,'Sequences': sequences}
cazy_df = pd.DataFrame(data = cazy_dict)

cazy_df.to_csv(r'C:\\Users\\Maninho\\Desktop\\CAZY\\cazy_df_v3.csv', header=True, sep=';')