package com.oops.store.service.impl;

import com.oops.store.entity.UserEntity;
import com.oops.store.mapper.UserMapper;
import com.oops.store.service.IUserService;
import com.oops.store.util.HashUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class UserServiceImpl implements IUserService {
    @Autowired
    private UserMapper user;

    @Override
    public UserEntity findUser(Integer userId, String userName, String userEmail) {
        if (userId != null)
            return user.findById(userId);
        else if (userName != null)
            return user.findByUserName(userName);
        else if (userEmail != null)
            return user.findByUserEmail(userEmail);
        return null;
    }

    @Override
    public List<UserEntity> findAllUser() {
        return user.findAll();
    }

    @Transactional
    @Override
    public void addUser(String userEmail, String userName, String userPassword) {
        UserEntity obj = new UserEntity();
        obj.setUserName(userName);
        obj.setUserEmail(userEmail);
        obj.setUserPassword(HashUtil.sha256(userPassword));
        user.add(obj);
    }
}
