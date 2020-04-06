package com.oops.store.mapper;

import com.oops.store.entity.BookEntity;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface BookMapper {
    public List<BookEntity> findAll();

    public BookEntity findById(@Param("bookId") int bookId);

    public List<BookEntity> findByName(@Param("bookName") String bookName);
}
