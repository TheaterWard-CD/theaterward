package com.abcd.theaterward.service;


import com.abcd.theaterward.domain.Theater;
import com.abcd.theaterward.repository.JpaTheaterRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TheaterService {

    private final JpaTheaterRepository jpaTheaterRepository;

    public TheaterService(JpaTheaterRepository jpaTheaterRepository) {
        this.jpaTheaterRepository = jpaTheaterRepository;
    }

    public List<Theater> findTheaters() {
        return jpaTheaterRepository.findAll();
    }
}
