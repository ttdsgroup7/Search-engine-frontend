//package top.caohongchuan.newsearch;
//
//import com.fasterxml.jackson.databind.ObjectMapper;
//import org.junit.jupiter.api.Test;
//import org.junit.runner.RunWith;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.test.context.SpringBootTest;
//import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;
//import org.springframework.data.redis.core.*;
//import org.springframework.test.context.junit4.SpringRunner;
//import org.springframework.util.Assert;
//
//import javax.annotation.Resource;
//import java.util.HashMap;
//import java.util.Map;
//
//
//@SpringBootTest
//public class TestRedis {
//
//    @Autowired
//    private RedisTemplate redisTemplate;
//    @Autowired
//    private StringRedisTemplate stringredisTemplate;
//
//    @Test
//    public void test() throws Exception {
//        HashOperations<String, String, String> opsForHash = redisTemplate.opsForHash();
//        Map<String, String> docid = opsForHash.entries("1");
//        System.out.println(docid);
//    }
//
//    @Test
//    public void test1() throws Exception {
//        ValueOperations<String, String> opsForValue = stringredisTemplate.opsForValue();
//        opsForValue.set("me", "2");
//        String docid = opsForValue.get("word");
//        System.out.println(docid);
//    }
//
//
//}
