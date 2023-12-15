package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Theater;

import java.util.List;
import java.util.Optional;

public interface TheaterRepository {
    List<Theater> findAll();

    Optional<Theater> findByName();
}
