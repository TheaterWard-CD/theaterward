package com.abcd.theaterward.domain;

import jakarta.persistence.*;

@Entity
@Table(name = "reviews")
public class Reviews {
    @Id
    @Column(name = "reviews_no")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int reviewNo;

    @Column(name = "users_id")
    private String userId;

    @Column(name = "reviews_score")
    private int reviewScore;

    @Column(name = "reviews_content")
    private String reviewContent;

    public int getReviewNo() {
        return reviewNo;
    }

    public void setReviewNo(int reviewNoo) {
        this.reviewNo = reviewNoo;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public int getReviewScore() {
        return reviewScore;
    }

    public void setReviewScore(int reviewScore) {
        this.reviewScore = reviewScore;
    }

    public String getReviewContent() {
        return reviewContent;
    }

    public void setReviewContent(String reviewContext) {
        this.reviewContent = reviewContext;
    }
}
