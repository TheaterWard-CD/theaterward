package com.abcd.theaterward.service;

import com.abcd.theaterward.domain.Show;
import com.abcd.theaterward.repository.JpaShowRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ShowService {
    private final JpaShowRepository jpaShowRepository;

    public ShowService(JpaShowRepository jpaShowRepository) {
        this.jpaShowRepository = jpaShowRepository;
    }

    public List<Show> findShows() {
        return jpaShowRepository.findAll();
    }
}
