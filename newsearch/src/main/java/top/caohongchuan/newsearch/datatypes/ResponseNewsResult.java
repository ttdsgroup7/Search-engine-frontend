package top.caohongchuan.newsearch.datatypes;

import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import org.springframework.stereotype.Component;
import scala.reflect.internal.Trees;

import java.util.ArrayList;
import java.util.List;

@Data
@Component
public class ResponseNewsResult {

    @ApiModelProperty(value = "News info")
    private List<NewsResult> newsarray;
}
