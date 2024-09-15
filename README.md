# podcast_transcripts
Interact (Search, Ask Questions, &amp; Chat) with Podcast Transcripts

You need to create a .env file in the project directory with the following:
VECTARA_API_KEY=your_Vectara_API_key  
VECTARA_CORPUS_KEY=SGU_Discourse_3

Run the following command to start:
chainlit run app.py -w

----------------

SGU-Parse.ipynb is the Jupyter Notebook with the code that downloads, parses, and saves the transcripts.  
SGU-Index.ipynb is the Jupyter Notebook with the code that Indexes/Uploads the transcripts to Vectara.  
ep_files contains the raw html files downloaded from the SGU Transcripts website.  
ep_json contains the json files with the json objects created by parsing the raw html into Vectara Document format.  
