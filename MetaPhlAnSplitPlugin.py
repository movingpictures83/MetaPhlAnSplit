import pandas as pd


class MetaPhlAnSplitPlugin:
    def input(self, inputfile):
       self.df = pd.read_csv(inputfile, sep='\t')

    def run(self):
       self.df['level'] = self.df['clade_name'].apply(lambda x: x.split('|')[-1][0])

    def output(self, outputfile):
       for level in self.df['level'].unique():
          df_tmp = self.df[self.df['level']==level]
          df_tmp = df_tmp.drop('level', axis=1)
          df_tmp.to_csv(outputfile+level +'.csv', index=False)
