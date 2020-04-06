package com.oops.store.controller;

import com.oops.store.entity.UserEntity;
import com.oops.store.service.IUserService;
import com.oops.store.util.HashUtil;
import com.oops.store.util.RetMessage;
import com.oops.store.util.jwt.JWTUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TokensController {
    @Autowired
    private IUserService user;

    @PostMapping(value = "/api/tokens")
    public RetMessage signIn(@RequestParam("userName") String userName,
                             @RequestParam("userPassword") String userPassword) {
        RetMessage ret = new RetMessage();

        UserEntity obj = user.findUser(null, userName, null);
        if (obj != null && obj.getUserPassword().equals(HashUtil.sha256(userPassword))) {
            if (obj.getUserStatus() == 1) {
                ret.setCode(2);
                ret.setMsg("Your account has been frozen!");
            } else {
                ret.setData(JWTUtil.createJWT(3600000, obj));
            }
        } else {
            ret.setCode(1);
            ret.setMsg("Username or password is invalid!");
        }
        return ret;
    }
}
