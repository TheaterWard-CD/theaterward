package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Seat;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

public interface SeatRepository {
    List<Seat> findAll();

    List<Seat> findByTheaterNo(int theater_no);
}
