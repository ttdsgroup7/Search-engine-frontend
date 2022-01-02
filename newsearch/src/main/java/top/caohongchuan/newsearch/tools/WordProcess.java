package top.caohongchuan.newsearch.tools;

import opennlp.tools.stemmer.PorterStemmer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import top.caohongchuan.newsearch.dao.TFIDF;

import java.util.HashSet;

@Component
public class WordProcess {

    @Autowired
    TFIDF tfidf;

    HashSet<String> stopwords;

    public String dealWord(String word){
        getStopWord();
        if(stopwords.contains(word)){
            return "STOPWORD";
        }
        PorterStemmer porterStemmer = new PorterStemmer();
        String wordStem = porterStemmer.stem(word);
        return wordStem;
    }

    public void getStopWord(){
        if(stopwords==null){
            stopwords = tfidf.getStopWord();
        }
    }
}
