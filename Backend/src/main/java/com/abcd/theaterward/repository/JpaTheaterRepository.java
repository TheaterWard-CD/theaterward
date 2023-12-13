package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Member;
import com.abcd.theaterward.domain.Theater;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;


@Repository
public class JpaTheaterRepository implements TheaterRepository{

    private final EntityManager em;

    public JpaTheaterRepository(EntityManager em) {
        this.em = em;
    }


    @Override
    public List<Theater> findAll() {
        return em.createQuery("select t from Theater t", Theater.class)
                .getResultList();
    }

    @Override
    public Optional<Theater> findByName() {
        return Optional.empty();
    }
}
