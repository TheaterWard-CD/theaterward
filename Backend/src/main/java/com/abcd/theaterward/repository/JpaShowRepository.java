package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Show;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class JpaShowRepository implements ShowRepository {
    private final EntityManager em;

    public JpaShowRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public List<Show> findAll() {
        return em.createQuery("select s from Show s", Show.class).getResultList();
    }
}
