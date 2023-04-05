# ComputationalBiophysics Term project

### Instructions for Running the Scrapper:    
1. Install all required modules with `pip install -r requirements.txt`.     
2. Download suitable chrome driver version from 'https://chromedriver.chromium.org/downloads'    
3. Change the path to chromedriver in `imgt_scrape.py` to the path where chrome driver is present.    
4. Run the imgt_scrape.py file to scrape all the data for humans & pMH1 from IMGT-3Dstructure-DB website.    
5. Run the process_imgt.py file to get the fasta files from the scraped data.    
6. Perform multiple sequence aligments for all the fasta files and save results in aligned_hla folder.    
7. Run the process_aligned_hla.py file to get the consensus paratope for each MHC ligand and the fasta file corresponding to that.
8. Perform multiple sequence aligment for the fasta file and save result in hla_msa.txt in the format '{MHC Ligand 4 digit Name}   {Paratope sequence}'.     

