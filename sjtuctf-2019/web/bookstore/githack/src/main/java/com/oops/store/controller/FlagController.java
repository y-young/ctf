package com.oops.store.controller;

import com.oops.store.service.IFlagService;
import com.oops.store.util.RetMessage;
import com.oops.store.util.jwt.AdminToken;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FlagController {
    @Autowired
    private IFlagService flag;

    @AdminToken
    @GetMapping(value = "/api/flag")
    public RetMessage getUser() {
        RetMessage ret = new RetMessage();
        ret.setData(flag.findFlag());
        return ret;
    }
}