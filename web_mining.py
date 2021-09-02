#!/usr/bin/env python
# coding: utf-8

# In[98]:


from pprint import pprint
from gensim import corpora,models,similarities


# In[99]:


documents=["new york times","new york post","los angeles times"]
tokenized_documents=[[token for token in document.lower().split()] for document in documents ]
pprint(tokenized_documents)


# In[100]:


dictionary=corpora.Dictionary(tokenized_documents)
print(dictionary)
print('\n')
print("number of documents :",dictionary.num_docs)


# In[101]:


words_and_indexes=dictionary.token2id

print(words_and_indexes)

print('\n', dictionary[0], dictionary[1])


# In[102]:


corpus_doc2bow_vectors=[dictionary.doc2bow(tok_doc) for tok_doc in tokenized_documents]
print("doc2bow_vectors of the three documents:[(id_words,tf), (id_word,tf),....,(id_word,tf)]")
temp=1
for c in corpus_doc2bow_vectors :
    print("\n*** The Document number :(",temp,")***")
    for i in c:
        id_word,tf=i
        print(f"The word:\'{dictionary[id_word]}\' --- The id_word :{id_word} --- TF:{tf}")
        
    temp+=1


# In[103]:


get_ipython().run_line_magic('time', 'tfidf_model = models.TfidfModel(corpus_doc2bow_vectors, id2word=dictionary, normalize=False)')
corpus_tfidf_vectors=tfidf_model[corpus_doc2bow_vectors]
print("----  tfidf_vectors of the three documents:[(id_word,tf), (id_word,tf),....,(id_word,)]  ----") 
com=1
for doc_vector in corpus_tfidf_vectors :
    
    print("\n*** The Document number :(",com,")***")
    for d in doc_vector:
        id_word,Tf_Idf=d
        print(f"The word:\'{dictionary[id_word]}\' --- The id_word :{id_word} --- Tf_Idf: {Tf_Idf}")
        
    com+=1
   


# In[113]:


query = "new new times"
query_bow_vector = dictionary.doc2bow(query.lower().split())

for (k,j) in query_bow_vector:
    
    print(f"The word_Id :{k} ---- occures :{j} time(s)")


# In[114]:


query_tfidf_vector = tfidf_model[query_bow_vector] 

for (kk,tf_Idf) in query_tfidf_vector:
 
    print(f"The word_Id :{kk} ---- TF_IDF :{tf_Idf}")


# In[115]:


index_matrix = similarities.SparseMatrixSimilarity(corpus_tfidf_vectors,num_features=6)
sims = index_matrix[query_tfidf_vector]
for (indexx,sim) in list(enumerate(sims)):
  
    print("Similarity between the query and the document number:",indexx," is :",sim)

