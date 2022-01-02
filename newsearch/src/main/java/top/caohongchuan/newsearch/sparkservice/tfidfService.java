package top.caohongchuan.newsearch.sparkservice;

import lombok.extern.slf4j.Slf4j;
import org.apache.spark.sql.SparkSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

@Slf4j
public class tfidfService {

    @Autowired
    private SparkSession sparkSession;

    public void test(){
        Dataset<Row> df = sparkSession.read().json("student.json");
        df.show();
    }

}
