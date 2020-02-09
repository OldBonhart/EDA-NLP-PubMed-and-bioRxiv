from .words_cloud import *
from .w2v_tsne import *
from .data_ploting import *
from .get_pdf import *

import nltk
from nltk.corpus import stopwords


def main(p_data, b_data,
         p_gif_name,b_gif_name,
         b_wc_name,p_wc_name,
         b_wc_name_mask,p_wc_name_mask,
         b_pdf_name,p_pdf_name,
         b_site,p_site, b_2d_name1,
         b_2d_name2, p_2d_name1,
         p_2d_name2, b_sim_name, 
         p_sim_name, theme,
          mask, img_promo):

    pubmed_sentences = get_sentences(p_data, "pubmed")
    biorxiv_sentences = get_sentences(b_data, "bioarchiv")
    biorxiv_model = Word2Vec(biorxiv_sentences,
                       size=200,
                       window=5,
                       min_count=3, 
                       workers=multiprocessing.cpu_count())
    pubmed_model = Word2Vec(pubmed_sentences,
                       size=200,
                       window=5,
                       min_count=3, 
                       workers=multiprocessing.cpu_count())

    biorxiv_embeddings, biorxiv_words = get_embedds_and_words(biorxiv_model)
    pubmed_embeddings, pubmed_words = get_embedds_and_words(pubmed_model)

    biorxiv_embeddings_2d = get_tsna_2d(biorxiv_embeddings)
    biorxiv_embeddings_3d = get_tsna_3d(biorxiv_embeddings)

    pubmed_embeddings_2d = get_tsna_2d(pubmed_embeddings)
    pubmed_embeddings_3d = get_tsna_3d(pubmed_embeddings)
    
    tsne_plot_2d(filename=b_2d_name1,
                 label='Visualizing Embeddings using t-SNE',
                 embeddings=pubmed_embeddings_2d,
                 a=0.4)
    tsne_plot_2d(filename=b_2d_name2,
                 label='Visualizing Embeddings using t-SNE',
                 embeddings=pubmed_embeddings_2d,
                 words=pubmed_words,
                 a=0.4)
    
    tsne_plot_2d(filename=p_2d_name1,
                 label='Similar words on the topic "{theme}',
                 embeddings=biorxiv_embeddings_2d, 
                 a=0.4)
    tsne_plot_2d(filename=p_2d_name2,
                 label='Similar words on the topic "{theme}',
                 embeddings=biorxiv_embeddings_2d,
                 words=biorxiv_words, 
                 a=0.4)

    tsne_plot_3d_gif(title=f'Visualizing Word Embeddings using t-SNE', 
                     label=f'Papers from the "{b_site}" on the topic -"{theme}"',
                     embeddings=biorxiv_embeddings_3d, 
                     filename=b_gif_name)
    
    tsne_plot_3d_gif(title=f'Visualizing Word Embeddings using t-SNE', 
                     label= f'Papers from the "{p_site}" on the topic -"{theme}"',
                     embeddings=pubmed_embeddings_3d, 
                     filename=p_gif_name)
    
    b_keys, b_embeddings_2d, b_word_clusters =  get_2d_clusters(biorxiv_model, k_words=30, n_top_words=25)
    p_keys, p_embeddings_2d, p_word_clusters =  get_2d_clusters(pubmed_model, k_words=30, n_top_words=25)

    tsne_plot_similar_words(f'Similar words from {b_site} on the topic {theme}',
                            b_keys,
                            b_embeddings_2d,
                            b_word_clusters,
                            0.7,
                            b_sim_name)
    tsne_plot_similar_words(f'Similar words from {p_site} on the topic {theme}',
                            p_keys,
                            p_embeddings_2d,
                            p_word_clusters,
                            0.7,
                            p_sim_name)
    
    biorxiv = makeWordCloud(10000000, 
                        b_data,
                        b_wc_name)

    biorxiv_with_mask = makeWordCloud(10000000,
                                b_data,
                                b_wc_name_mask,
                                mask=mask)
    
    pubmed = makeWordCloud(10000000, 
                       p_data,
                       p_wc_name)

    pubmed_with_mask = makeWordCloud(10000000,
                                     p_data,
                                     p_wc_name_mask,
                                     mask=mask)
    
    make_pdf(site=p_site,
            MAP=p_data,
            pdf_name=p_pdf_name,
            wc_name=p_wc_name,
            wc_name_mask=p_wc_name_mask,
            name1_2d = p_2d_name1,
            name2_2d = p_2d_name2,
            sim_name=p_sim_name,
            gif_name=p_gif_name,
            img_promo=img_promo)

    make_pdf(site=b_site,
            MAP=b_data,
            pdf_name=b_pdf_name,
            wc_name=b_wc_name,
            wc_name_mask=b_wc_name_mask,
            name1_2d = b_2d_name1,
            name2_2d = b_2d_name2,
            sim_name=b_sim_name,
            gif_name=b_gif_name,
            img_promo=img_promo)

    print("Done!")
