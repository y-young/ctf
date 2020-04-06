package com.oops.store.service.impl;

import com.oops.store.entity.BookEntity;
import com.oops.store.mapper.BookMapper;
import com.oops.store.service.IBookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookServiceImpl implements IBookService {
    @Autowired
    BookMapper book;

    @Override
    public BookEntity findById(int bookId) {
        return book.findById(bookId);
    }

    @Override
    public List<BookEntity> findAll() {
        return book.findAll();
    }

    @Override
    public List<BookEntity> findByName(String bookName) {
        return book.findByName(bookName);
    }
}
