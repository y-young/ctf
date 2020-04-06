package com.oops.store.service;

import com.oops.store.entity.UserEntity;

import java.util.List;

public interface IUserService {
    public UserEntity findUser(Integer userId, String userName, String userEmail);

    public List<UserEntity> findAllUser();

    public void addUser(String userEmail, String userName, String userPassword);
}
