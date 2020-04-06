package com.oops.store.controller;

import com.oops.store.entity.BookEntity;
import com.oops.store.service.IBookService;
import com.oops.store.util.RetMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@RestController
public class BookController {
    @Autowired
    private IBookService book;

    @GetMapping(value = "/api/books")
    public RetMessage getBooks(@RequestParam(value = "bookId", required = false) Integer bookId,
                               @RequestParam(value = "bookName", required = false) String bookName) {
        RetMessage ret = new RetMessage();
        if (bookId != null) {
            BookEntity data = book.findById(bookId);
            if (data == null) {
                ret.setCode(1);
                ret.setMsg("Book not exists!");
            }
            ret.setData(data);
        } else if (bookName != null) {
            try {
                ret.setData(book.findByName(bookName));
            } catch (Exception e) {
                ret.setData(new ArrayList<BookEntity>());
            }
        } else {
            ret.setData(book.findAll());
        }
        return ret;
    }
}
