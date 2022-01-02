package top.caohongchuan.newsearch.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.*;
import org.springframework.stereotype.Repository;

import java.util.*;

@Repository
public class TFIDF {

    @Autowired
    private StringRedisTemplate stringredisTemplate;

    public HashMap<String, String> getTFIDF(String word){
        HashOperations<String, String, String> opsForHash = stringredisTemplate.opsForHash();
        Map<String, String> docid = opsForHash.entries(word);
        return (HashMap<String, String>)docid;
    }

    public HashSet<String> getStopWord(){
        ListOperations<String, String> opsForList = stringredisTemplate.opsForList();
        List<String> stopwordlist = opsForList.range("STOPWRODS", 0, -1);
        HashSet<String> stopword = new HashSet<>(stopwordlist);
        return stopword;
    }


}
