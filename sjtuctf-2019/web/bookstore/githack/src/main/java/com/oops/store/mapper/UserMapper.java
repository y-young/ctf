package com.oops.store.mapper;

import com.oops.store.entity.UserEntity;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface UserMapper {
    public List<UserEntity> findAll();

    public UserEntity findById(@Param("userId") int userId);

    public UserEntity findByUserName(@Param("userName") String userName);

    public UserEntity findByUserEmail(@Param("userEmail") String userEmail);

    public int add(UserEntity user);
}
