//package top.caohongchuan.newsearch;
//
//import org.junit.jupiter.api.Test;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.test.context.SpringBootTest;
//import top.caohongchuan.newsearch.dao.NewsRetrieve;
//import top.caohongchuan.newsearch.datatypes.NewsResult;
//
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.List;
//
//@SpringBootTest
//public class TestMysql {
//
//    @Autowired
//    NewsRetrieve newsRetrieve;
//
//    @Test
//    public void mysqlTest(){
//        ArrayList<String> docids = new ArrayList<>();
//        docids.add("1");
//        docids.add("2");
//        docids.add("3");
//        List<NewsResult> res = newsRetrieve.getNews(docids);
//        System.out.println(res);
//    }
//}
