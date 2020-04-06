package com.oops.store.mapper;

import com.oops.store.entity.FlagEntity;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface FlagMapper {
    public FlagEntity getFlag();
}
