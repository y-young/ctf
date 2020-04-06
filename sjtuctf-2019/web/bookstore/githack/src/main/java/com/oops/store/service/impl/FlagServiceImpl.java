package com.oops.store.service.impl;

import com.oops.store.entity.FlagEntity;
import com.oops.store.mapper.FlagMapper;
import com.oops.store.service.IFlagService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class FlagServiceImpl implements IFlagService {
    @Autowired
    FlagMapper flag;

    @Override
    public FlagEntity findFlag() {
        return flag.getFlag();
    }
}
