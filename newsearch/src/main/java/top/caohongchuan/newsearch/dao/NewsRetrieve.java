package top.caohongchuan.newsearch.dao;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import top.caohongchuan.newsearch.datatypes.NewsResult;
import top.caohongchuan.newsearch.datatypes.ResponseNewsResult;

import java.util.ArrayList;
import java.util.List;

@Mapper
public interface NewsRetrieve {

    @Select({
            "<script> ",
            "select publish_date, head_line, tag from BBC_news",
            "<where> ",
            "docid in",
            "<foreach item='item' index='index' collection='docids' open='(' separator=',' close=')'> ",
            "#{item} ",
            "</foreach>",
            "</where>",
            "</script>"
    })
    public List<NewsResult> getNews(@Param("docids") ArrayList<String> docids);
}
