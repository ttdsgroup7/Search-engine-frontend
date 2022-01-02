//package top.caohongchuan.newsearch;
//
//import lombok.extern.slf4j.Slf4j;
//import org.apache.spark.SparkContext;
//import org.apache.spark.api.java.JavaRDD;
//import org.apache.spark.api.java.JavaSparkContext;
//import org.apache.spark.sql.Dataset;
//import org.apache.spark.sql.Row;
//import org.apache.spark.sql.SparkSession;
//import org.junit.jupiter.api.Test;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.test.context.SpringBootTest;
//
//@Slf4j
//@SpringBootTest
//public class SparkTest {
//    @Autowired
//    private SparkSession sparkSession;
//    @Autowired
//    private JavaSparkContext javaSparkContext;
//
//    @Test
//    public void test(){
//        Dataset<Row> df = sparkSession.read().json("/home/yingzheng2/student.json");
//        log.warn(df.toString());
//    }
//
//    @Test
//    public void test_RDD(){
//        JavaRDD<String> data = javaSparkContext.textFile("/home/yingzheng2/teacher.txt");
//        log.warn(data.first());
//    }
//}
