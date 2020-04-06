package com.oops.store.entity;

import org.springframework.stereotype.Component;

@Component
public class FlagEntity {
    private String flag;

    public String getFlag() {
        return flag;
    }

    public void setFlag(String flag) {
        this.flag = flag;
    }
}
