package top.caohongchuan.newsearch.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import top.caohongchuan.newsearch.datatypes.ResponseNewsResult;
import top.caohongchuan.newsearch.service.SearchService;

@RestController
@RequestMapping(value = "/search")
@Api(tags = "Search API")
public class SearchController {

    @Autowired
    SearchService searchService;

    @ApiOperation("Send one query to server")
    @GetMapping("/querynews")
    public ResponseNewsResult query(@RequestParam("query") String querystr){
        ResponseNewsResult responseNewsResult = searchService.dealquery(querystr);
        return responseNewsResult;
    }
}
