package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Show;

import java.util.List;

public interface ShowRepository {
    List<Show> findAll();
}
