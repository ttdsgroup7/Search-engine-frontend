//package top.caohongchuan.newsearch;
//
//import org.junit.jupiter.api.Test;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.test.context.SpringBootTest;
//import top.caohongchuan.newsearch.controller.SearchController;
//import top.caohongchuan.newsearch.dao.TFIDF;
//import top.caohongchuan.newsearch.datatypes.ResponseNewsResult;
//
//@SpringBootTest
//class NewsearchApplicationTests {
//
//	@Autowired
//	SearchController searchController;
//	@Autowired
//	TFIDF tfidf;
//
//	@Test
//	void contextLoads() {
//		ResponseNewsResult responseNewsResult = searchController.query("google OR trump");
//		System.out.println(responseNewsResult.getNewsarray());
//	}
//
//	@Test
//	void loadtfidf(){
//		tfidf.getTFIDF("trump");
//	}
//
//}
