package top.caohongchuan.newsearch.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import top.caohongchuan.newsearch.dao.NewsRetrieve;
import top.caohongchuan.newsearch.datatypes.ResponseNewsResult;
import top.caohongchuan.newsearch.tools.ParseQuery;
import top.caohongchuan.newsearch.tools.SearchEngine;

import java.util.ArrayList;

@Service
public class SearchService {

    @Autowired
    ParseQuery parseQuery;
    @Autowired
    SearchEngine searchService;
    @Autowired
    NewsRetrieve newsRetrieve;

    public ResponseNewsResult dealquery(String querystr){
        ArrayList<String> postexpr = parseQuery.getPostExpr(querystr);
        ArrayList<String> docids = searchService.docIdFromPostExpr(postexpr);
        ResponseNewsResult responseNewsResult = new ResponseNewsResult();
        responseNewsResult.setNewsarray(newsRetrieve.getNews(docids));
        return responseNewsResult;
    }
}
