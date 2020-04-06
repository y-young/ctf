package com.oops.store.controller;

import com.oops.store.service.IUserService;
import com.oops.store.util.RetMessage;
import com.oops.store.util.jwt.AdminToken;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private IUserService user;

    @GetMapping(value = "/api/userVerify")
    public RetMessage verifyUser(@RequestParam(value = "userId", required = false) Integer userId,
                                 @RequestParam(value = "userName", required = false) String userName,
                                 @RequestParam(value = "userEmail", required = false) String userEmail) {
        RetMessage ret = new RetMessage();

        if (userId != null || userName != null || userEmail != null) {
            if (user.findUser(userId, userName, userEmail) != null) {
                ret.setCode(1);
                ret.setMsg("User already exists!");
            }
        } else {
            ret.setCode(2);
            ret.setMsg("No condition exists!");
        }
        return ret;
    }

    @AdminToken
    @GetMapping(value = "/api/users")
    public RetMessage getUser() {
        RetMessage ret = new RetMessage();
        ret.setData(user.findAllUser());
        return ret;
    }

    @PostMapping(value = "/api/users")
    public RetMessage signUp(@RequestParam("userEmail") String userEmail,
                             @RequestParam("userName") String userName,
                             @RequestParam("userPassword") String userPassword) {
        if (userPassword.length() < 6)
            return new RetMessage(3, "Password is too short!");
        if (user.findUser(null, null, userEmail) != null)
            return new RetMessage(1, "Email already exists!");
        if (user.findUser(null, userName, null) != null)
            return new RetMessage(2, "Username already exists!");

        user.addUser(userEmail, userName, userPassword);
        return new RetMessage();
    }
}