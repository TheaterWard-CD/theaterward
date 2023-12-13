package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Ssr;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
public class JpaSsrRepository implements SsrRepository{

    @PersistenceContext
    EntityManager em;


    @Override
    @Transactional
    public void save(Ssr ssr) {
        em.persist(ssr);
    }
}
