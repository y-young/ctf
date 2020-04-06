package com.oops.store.service;

import com.oops.store.entity.BookEntity;

import java.util.List;

public interface IBookService {
    public BookEntity findById(int bookId);

    public List<BookEntity> findAll();

    public List<BookEntity> findByName(String bookName);
}
