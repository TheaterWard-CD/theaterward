package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Users;

public interface UserRepository {
    public long dupe(String userId);

    public Users save(Users users);

    public Users findById(String userId);
}
