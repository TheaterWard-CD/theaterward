package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Member;

import java.util.List;

public interface MemberRepository {
    List<Member> findAll();
}
